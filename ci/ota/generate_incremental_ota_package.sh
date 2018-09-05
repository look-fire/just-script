#!/bin/bash
#Transsion Top Secret
#  generate_incremental_ota_package.sh: as the name says
#  DO NOT PRINT SMB_PASSWD
#  DO NOT USE ANY smbclient WRITE METHOD HERE

###############################
###### CONSTANTS SECTION ######
###############################
# passed by environment variable, DO NOT UNSET
declare SMB_USER
declare SMB_PASSWD
readonly OPTION_VAR_ARRAY=(
    OTA_TOOLS
    INCREMENTAL_FROM
    BLOCK_MODE
    INPUT_TARGET_FILE
    OUTPUT_OTA_PACKAGE
    DEVICE_SPECIFIC
    PACKAGE_ZIP_FILE_PATH
    MD5SUM_FILE_PATH
    OTA_TEMPDIR
)


########################################
###### FUNCTION DECLARATION SECTION  ###
########################################
function log(){
    local -r MODE=$1
    shift
    echo "$(date '+%Y-%m-%d %H:%M:%S') $MODE: $*"
}


function log_info(){
    log "INFO" "$@"
}


function log_warning(){
    log "WARNING" "$@"
}


function log_error(){
    # NOTICE: when calling log_error, the build process should be regarded as failure
    log "ERROR" "$@"
}


function myrealpath(){
    local -r path="$1"
    if [ ! -z "$path" ]
    then
        python -c "import os; print os.path.abspath('${path}')"
    else
        echo ""
    fi
}


function all_switch(){
    for arg in "$@"
    do
        if [[ "$arg" != "true" && "$arg" != "false" ]]
        then
            return 1
        fi
    done
    return 0
}


function is_safe_path(){
    local -r path="$1"
    python - "${path}" <<EOF
import sys
if len(sys.argv[1]) == 0:
    sys.exit(1)
validchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+,-./@_'
result = all(c in validchars for c in sys.argv[1])
if result:
    sys.exit(0)
else:
    sys.exit(1)
EOF
    return $?
}


function clean_environment(){
    for myvar in "${OPTION_VAR_ARRAY[@]}"
    do
        unset "$myvar"
    done
}

function make_tempdir(){
    OTA_TEMPDIR="$(myrealpath "$(mktemp -t --directory OTA_TMP_DIR_"$(date +%Y%m%d%H%M)"_XXXXXX)")"
    if [ ! -d "${OTA_TEMPDIR}" ]
    then
        log_error "invalid ota tempdir: ${OTA_TEMPDIR}, exit abnormally"
    fi

    readonly OTA_TEMPDIR
    export OTA_TEMPDIR
}

function parse_arguments(){
    # create OTA_TEMPDIR
    make_tempdir

    while [[ $# -gt 1 ]]
    do
        key="$1"

        case "$key" in
            --block)
                readonly BLOCK_MODE="$2"
                all_switch "${BLOCK_MODE}"
                if [ "$?" != 0 ]
                then
                    log_error "--block should be true or false, exit abnormally"
                    exit 1
                fi
                readonly BLOCK_MODE
                ;;
            --device-specific)
                readonly DEVICE_SPECIFIC="$2"
                all_switch "${DEVICE_SPECIFIC}"
                if [ "$?" != 0 ]
                then
                    log_error "--device-specific should be true or false, exit abnormally"
                    exit 1
                fi
                readonly DEVICE_SPECIFIC
                ;;
            --output-otapackage)
                readonly OUTPUT_OTA_PACKAGE=$(myrealpath "$2")
                is_safe_path "${OUTPUT_OTA_PACKAGE}"
                if [ "$?" != 0 ]
                then
                    log_error "output ota package name not safe: ${OUTPUT_OTA_PACKAGE}, exit abnormally"
                    exit 1
                fi

                if [ -e "${OUTPUT_OTA_PACKAGE}" ]
                then
                    log_error "output ota package already exists: ${OUTPUT_OTA_PACKAGE}, exit abnormally"
                    exit 1
                fi

                local -r outputdir=$(dirname "${OUTPUT_OTA_PACKAGE}")
                if [ ! -d "${outputdir}" ]
                then
                    log_error "invalid directory: ${outputdir}, exit abnormally"
                    exit 1
                fi
                ARCHIVE_DATE="$(date +%Y%m%d%H%M%S)"
                PACKAGE_ZIP_FILE_PATH="${outputdir}"/package_"$ARCHIVE_DATE".zip
                MD5SUM_FILE_PATH="${outputdir}"/md5sum
                log_info "otapackage to be generated: ${OUTPUT_OTA_PACKAGE}"
                log_info "md5sum file to be generated: ${MD5SUM_FILE_PATH}"
                log_info "packaged otapackage to be generated: ${PACKAGE_ZIP_FILE_PATH}"

                if [ -e "${PACKAGE_ZIP_FILE_PATH}" ]
                then
                    log_error "packaged ota package already exists: ${PACKAGE_ZIP_FILE_PATH}, exit abnormally"
                    exit 1
                fi
                ;;
            --archive-base-dir)
                ARCHIVE_BASE_DIR="$2"
               # ARCHIVE_BASE_DIR_TEST=$(echo "$ARCHIVE_BASE_DIR" | sed 's#mnt#192.168.1.75#g')
                
                ;;
            --archive-product-dir-relative)
                ARCHIVE_PRODUCT_DIR_RELATIVE="$2"
                ;;             
            --incremental-from)
                INCREMENTAL_FROM_dir="$2"
                TRUE_INCREMENTAL_FROM="$2"
                if [[ -z "${SMB_USER+x}" || -z "${SMB_PASSWD+x}" ]]
                then
                    log_error "please set --smb-user and --smb-user before --incremental-from, exit abnormally"
                    exit 1
                fi
                INCREMENTAL_FROM_dir_temp=$(echo "$INCREMENTAL_FROM_dir"|sed 's/\\/\//g')
                INCREMENTAL_FROM_dir_all_files=$(get_target_dir_from_unc "$INCREMENTAL_FROM_dir_temp")
                INCREMENTAL_FROM_dir_full_file=$(math_target_files "$INCREMENTAL_FROM_dir_all_files")
                INCREMENTAL_FROM_temp="$INCREMENTAL_FROM_dir"\\"$INCREMENTAL_FROM_dir_full_file"
                INCREMENTAL_FROM=$(echo "${INCREMENTAL_FROM_temp}")
                log_info "${INCREMENTAL_FROM}"
                # normalize path
                if is_unc_file "${INCREMENTAL_FROM}"
                then
                    if [ -d "${OTA_TEMPDIR}" ]
                    then
                        pushd "${OTA_TEMPDIR}"
                            copy_unc_file "${INCREMENTAL_FROM}"
                            INCREMENTAL_FROM_OTA_TOOLS=$(get_ota_tools_path "${INCREMENTAL_FROM}")
                            FROM_OTA_NAME=$(get_base_ota_name "${INCREMENTAL_FROM}")
                            log_info "FROM_OTA_NAME is $FROM_OTA_NAME"
                            INCREMENTAL_FROM=$(myrealpath "$(get_filename_from_unc_path "${INCREMENTAL_FROM}")")
                        popd
                    else
                        log_error "invalid ota tempdir: ${OTA_TEMPDIR}, exit abnormally"
                    fi
                else
                    INCREMENTAL_FROM=$(myrealpath "${INCREMENTAL_FROM}")
                fi

                # file validation
                if [ ! -f "${INCREMENTAL_FROM}" ]
                then
                    if [ "${OTATEST}" == true ]
                    then
                       log_info "Now we do OTATEST automatic"
                    else
                       log_error "${INCREMENTAL_FROM} file not found, exit abnormally"
                       exit 1
                    fi
                else
                    log_info "INPUT_TARGET_FILE: $(ls -l "${INCREMENTAL_FROM}")"
                fi
                ;;
            --target)
                INPUT_TARGET_FILE_dir="$2"
                TRUE_INPUT_TARGET_FILE="$2"
                if [[ -z "${SMB_USER+x}" || -z "${SMB_PASSWD+x}" ]]
                then
                    log_error "please set --smb-user and --smb-user before --target, exit abnormally"
                    exit 1 
                fi
                INPUT_TARGET_FILE_dir_temp=$(echo "$INPUT_TARGET_FILE_dir"|sed 's/\\/\//g')
                INPUT_TARGET_FILE_dir_temp_all_files=$(get_target_dir_from_unc "$INPUT_TARGET_FILE_dir_temp")
                INPUT_TARGET_FILE_dir_temp_all_files_full_file=$(math_target_files "$INPUT_TARGET_FILE_dir_temp_all_files")
                INPUT_TARGET_FILE_temp="$INPUT_TARGET_FILE_dir"\\"$INPUT_TARGET_FILE_dir_temp_all_files_full_file"
                INPUT_TARGET_FILE=$(echo "${INPUT_TARGET_FILE_temp}")
                log_info "${INPUT_TARGET_FILE}"

                # normalize path
                if is_unc_file "${INPUT_TARGET_FILE}"
                then
                    if [ -d "${OTA_TEMPDIR}" ]
                    then
                        pushd "${OTA_TEMPDIR}"
                            copy_unc_file "${INPUT_TARGET_FILE}"
                            TARGET_OTA_NAME=$(get_base_ota_name "${INPUT_TARGET_FILE}")
                            INPUT_TARGET_OTA_TOOLS=$(get_ota_tools_path "${INPUT_TARGET_FILE}")
                            log_info "TARGET_OTA_NAME is : ${TARGET_OTA_NAME}"
                            INPUT_TARGET_FILE=$(myrealpath "$(get_filename_from_unc_path "${INPUT_TARGET_FILE}")")
                        popd
                    else
                        log_error "invalid ota tempdir: ${OTA_TEMPDIR}, exit abnormally"
                    fi
                else
                    INPUT_TARGET_FILE=$(myrealpath "${INPUT_TARGET_FILE}")
                fi
                # file validation
                if [ ! -f "${INPUT_TARGET_FILE}" ]
                then
                    if [ "${OTATEST}" == true ]
                    then
                       log_info "Now we do OTATEST automatic"
                    else
                       log_error "${INPUT_TARGET_FILE} file not found, exit abnormally"
                       exit 1
                    fi
                else
                    log_info "INPUT_TARGET_FILE: $(ls -l "${INPUT_TARGET_FILE}")"
                fi
                ;;
            --otatest)
                OTATEST="$2"
                ;;
            *)
                log_error "do not allow non-option command line arguments: $1, exit abnormally"
                ;;
        esac
        shift; shift # past option, do not support regular argument
    done

    # ensure all option variables are initialized
    for myvar in "${OPTION_VAR_ARRAY[@]}"
    do
        if [ -z "${myvar+x}" ]
        then
           log_error "${myvar} not set, must be given through command line, exit abnormally"
        fi
    done
}

function get_ota_tools_path(){
    local -r path=$1
    local -r p_dir=${path%\\*}
    local OTA_TOOLS=${p_dir}\\OTA_TOOLS.zip
    echo  "${OTA_TOOLS}"
}

function get_dir_parameters(){
    ARCHIVE_BASE_DIR=$( echo "$ARCHIVE_BASE_DIR"| sed 's#mnt#\/192.168.1.75#g')
    TARGET_DIR="$ARCHIVE_BASE_DIR"/"$ARCHIVE_PRODUCT_DIR_RELATIVE"
    log_info "$TARGET_DIR"
    all_dirs=$(get_target_dir_from_unc "$TARGET_DIR")
    log_info "$all_dirs"
    all_dirs_temp1=$(echo "$all_dirs" | awk -F " " '{print $1}' | sed -n '3,$p'| tac | sed -n '3,$p')
    all_dirs_temp2=$(echo "$all_dirs" | awk -F " " '{print $1}' | sed -n '3,$p'| tac | sed -n '3,$p'| sed -n '2,$p')
    for i in $all_dirs_temp1
    do
        local First_time=$i
        break
    done

    for i in $all_dirs_temp2
    do
        if [[ "$i" =~ "_error" ]] || [[ "$i" =~ "_ENG" ]]
        then
            continue
        else
            local Second_time=$i
            break
        fi
    done
    echo "Three"
    First_time_dir="$TARGET_DIR"/"$First_time"
    log_info "$First_time_dir"
    Second_time_dir="$TARGET_DIR"/"$Second_time"
    log_info "$Second_time_dir"    
}

function get_otatest_automatic(){

    log_info "Now we will do OTATEST automatic "
    
    get_dir_parameters

    First_time_dir_all_files=$(get_target_dir_from_unc "$First_time_dir")
    Second_time_dir_all_files=$(get_target_dir_from_unc "$Second_time_dir")

    Firtst_time_full_file=$(math_target_files "$First_time_dir_all_files")
    Second_time_full_file=$(math_target_files "$Second_time_dir_all_files")

    INCREMENTAL_FROM_temp="$First_time_dir"/"$Firtst_time_full_file"
    INCREMENTAL_FROM=$(echo "${INCREMENTAL_FROM_temp}")
    if is_unc_file "${INCREMENTAL_FROM}"
    then
        if [ -d "${OTA_TEMPDIR}" ]
        then
            pushd "${OTA_TEMPDIR}"
            copy_unc_file "${INCREMENTAL_FROM}"
            INCREMENTAL_FROM_OTA_TOOLS="${First_time_dir}"/OTA_TOOLS.zip
            
            FROM_OTA_NAME=$(get_base_ota_name "${INCREMENTAL_FROM}")
            log_info "FROM_OTA_NAME is $FROM_OTA_NAME"
            INCREMENTAL_FROM=$(myrealpath "$(get_filename_from_unc_path "${INCREMENTAL_FROM}")")
            popd
        else
            log_error "invalid ota tempdir: ${OTA_TEMPDIR}, exit abnormally"
        fi
    else
        INCREMENTAL_FROM=$(myrealpath "${INCREMENTAL_FROM}")
    fi

 
    INPUT_TARGET_FILE_temp="$Second_time_dir"/"$Second_time_full_file"
    INPUT_TARGET_FILE=$(echo "${INPUT_TARGET_FILE_temp}")
    if is_unc_file "${INPUT_TARGET_FILE}"
    then
        if [ -d "${OTA_TEMPDIR}" ]
        then
            pushd "${OTA_TEMPDIR}"
            copy_unc_file "${INPUT_TARGET_FILE}"
            TARGET_OTA_NAME=$(get_base_ota_name "${INPUT_TARGET_FILE}")
            log_info "TARGET_OTA_NAME is : ${TARGET_OTA_NAME}"
            INPUT_TARGET_FILE=$(myrealpath "$(get_filename_from_unc_path "${INPUT_TARGET_FILE}")")
            popd
        else
            log_error "invalid ota tempdir: ${OTA_TEMPDIR}, exit abnormally"
        fi
    else
        INPUT_TARGET_FILE=$(myrealpath "${INPUT_TARGET_FILE}")
    fi


    log_info "${INCREMENTAL_FROM}"
    log_info "${INPUT_TARGET_FILE}" 
   
}



function get_ota_tools(){
    if [ "${OTATEST}" == true ]
    then
        if [ ! -z "${TRUE_INCREMENTAL_FROM}" ] && [ ! -z "${TRUE_INPUT_TARGET_FILE}" ]
        then 
            log_info "Now we will do OTATEST by parameter of entering manually"
            OTA_TOOLS=${INCREMENTAL_FROM_OTA_TOOLS}
        else
            get_otatest_automatic
            OTA_TOOLS=${INCREMENTAL_FROM_OTA_TOOLS}
        fi
    else
        log_info "Now we will do OTA"
        OTA_TOOLS=${INPUT_TARGET_OTA_TOOLS}
    fi
    local -r TEMP=$(echo "$OTA_TOOLS"|sed 's/\\/\//g')
    OTA_ARCHIVE_DIR=${TEMP%\/*}
    log_info "OTA_ARCHIVE_DIR  is $OTA_ARCHIVE_DIR"
    if [[ -z "${SMB_USER+x}" || -z "${SMB_PASSWD+x}" ]]
    then
        log_error "please set --smb-user and --smb-user before --ota-tools, exit abnormally"
    fi

    # normalize path
    if is_unc_file "${OTA_TOOLS}"
    then
        if [ -d "${OTA_TEMPDIR}" ]
        then
            pushd "${OTA_TEMPDIR}"
            copy_unc_file "$OTA_TOOLS"
            OTA_TOOLS=$(myrealpath "$(get_filename_from_unc_path "$OTA_TOOLS")")
            popd
        else
            log_error "invalid ota tempdir: ${OTA_TEMPDIR}, exit abnormally"
        fi
     else
         OTA_TOOLS=$(myrealpath "${OTA_TOOLS}")
     fi

     # file validation
     if [ ! -f "${OTA_TOOLS}" ]
     then
         log_error "${OTA_TOOLS} file not found, exit abnormally"
         exit 1
     fi
     log_info "OTA_TOOLS: $(ls -l "${OTA_TOOLS}")"
}

function get_target_dir_from_unc(){
    local -r uncfile="$1"
    local -r dname="$uncfile"
    local -r index=$(echo "$dname"|grep -aob '/'|sed -n '4p'|cut -d ':' -f1)
    local servicename="${dname:0:index}"
    local relativedir="${dname:index+1}"
    local basecmd
    basecmd=("smbclient" "${servicename}" "-c" "cd \"${relativedir}\";ls")
    "${basecmd[@]}" -A=<(echo -e "username = ${SMB_USER}\npassword = ${SMB_PASSWD}")
}

function math_target_files(){
    local target_dir_files="$1"
    target_all_files=$(echo "$target_dir_files" | awk -F " " '{print $1}' | sed -n '3,$p'| tac | sed -n '3,$p')
    target_file=$( echo "$target_all_files" | grep  "full.*.zip")
    echo "$target_file"
} 

# accept '/' as path delimiter only
function download_from_unc(){
    # NOTICE:
    #     from https://www.samba.org/samba/docs/man/manpages/smbclient.1.html
    #         You can specify file names which have spaces in them by quoting the name with double quotes, for example "a long file name".

    local -r uncfile="$1"
    local -r fname=$(basename "$uncfile")
    local -r dname=$(dirname "$uncfile")
    # shellcheck disable=SC2034
    local -r index=$(echo "$dname"|grep -aob '/'|sed -n '4p'|cut -d ':' -f1)
    local servicename="${dname:0:index}"
    local relativedir="${dname:index+1}"

    local basecmd
    basecmd=("smbclient" "${servicename}" "-c" "cd \"${relativedir}\"; get \"${fname}\"")
    log_info "execute cmd now: ${basecmd[*]}"
    # do not use -U option to avoid password leak in "ps" output
    # use bash "process substitution" scheme to avoid password leak
    # the password here will not be shown in 'ps' output or any disk files
    "${basecmd[@]}" -A=<(echo -e "username = ${SMB_USER}\npassword = ${SMB_PASSWD}")
    return $?
    # yet another solution, not so secure as above:
    #     env USER="${SMB_USER}" PASSWD="${SMB_PASSWD}" "${basecmd[@]}"
}

function get_base_ota_name(){
    local path="$1"
    local -r uncfile=${path//\\/\/}
    local -r fname=$(basename "$uncfile")
    local -r dname=$(dirname "$uncfile")
    # shellcheck disable=SC2034
    local -r index=$(echo "$dname"|grep -aob '/'|sed -n '4p'|cut -d ':' -f1)
    local servicename="${dname:0:$index}"
    local relativedir="${dname:$index+1}"

    local from_basecmd
    from_basecmd=("smbclient" "${servicename}" "-c" "cd \"${relativedir}\"; ls Tcard_update*.zip")
    from_tcardname=$("${from_basecmd[@]}" -A=<(echo -e "username = ${SMB_USER}\npassword = ${SMB_PASSWD}"))
    from_tcardname=${from_tcardname#*Tcard_update_}
    BASE_OTA_NAME=${from_tcardname%.zip*}
    echo "${BASE_OTA_NAME}"

}

function upload_to_unc(){
    local -r local_file="$1"
    local -r unc_dir="$2"
    local -r unc_dir_file=$(basename "$unc_dir")
    local -r unc_dir_dir=$(dirname "$unc_dir")
    local -r index=$(echo "$unc_dir_dir"|grep -aob '/'|sed -n '4p'|cut -d ':' -f1)
    local servicename="${unc_dir_dir:0:$index}"
    local relativedir="${unc_dir_dir:$index+1}"
    local basecmd

    basecmd=("smbclient" "${servicename}" "-c" "cd \"${relativedir}\"; put \"${local_file}\" \"${unc_dir_file}\"")
    log_info "execute cmd now: ${basecmd[*]}"

    "${basecmd[@]}" -A=<(echo -e "username = ${SMB_USER}\npassword = ${SMB_PASSWD}")
    return $?
}

function is_unc_file(){
    local path="$1"
    path=$(echo "$path"|sed 's/\\/\//g')
    if [[ ${path:0:1} == '/' && ${path:1:1} == '/' ]]
    then
        return 0
    else
        return 1
    fi
}


function get_filename_from_unc_path(){
    local path="$1"
    path=$(echo "$path"|sed 's/\\/\//g')
    myrealpath "$(basename "$path")"
}


# copy unc file to current directory
function copy_unc_file(){
    local path="$1"
    path=$(echo "$path"|sed 's/\\/\//g')

    log_info "$path is in unc form, try to copy to local disk now"
    # normalize path
    local -r localfile=$(get_filename_from_unc_path "$path")
    download_from_unc "$path"
    if [[ "$?" != 0 || ! -s "$localfile" ]]
    then
        log_error "copy $path failed, exit abnormally"
        exit 1
    fi
}

function unzip_ota_tools(){
    log_info "unzip ota tools to ${OTA_TEMPDIR} now"

    unzip "${OTA_TOOLS}" -d "${OTA_TEMPDIR}"
}


function parse_ota_tools_dir(){
    log_info "parse ota tools to get necessary information now"

    pushd "${OTA_TEMPDIR}"
        local privatekeys=( $(find "$(pwd)" -name '*.pk8') )
        if [ "${#privatekeys[@]}" != 1 ]
        then
            log_error "there is more than one private key in ota tools, exit abnormally"
            exit 1
        fi
        RELEASE_KEY=${privatekeys[0]%*.pk8}
        readonly RELEASE_KEY

        OTA_SCRIPT=$(find "$(pwd)" -name ota_from_target_files)
        if [ -z "${OTA_SCRIPT}" ]
        then
            log_error "ota_from_target_files not found, exit abnormally"
            exit 1
        fi
        readonly OTA_SCRIPT

        local -r device_specific_script=$(find "$(pwd)" -name mt_ota_from_target_files.py)
        if [[ "${DEVICE_SPECIFIC}" == 'true' && -n "$device_specific_script" ]]
        then
            DEVICE_SPECIFIC_OPTION=("-s" "${device_specific_script%*.py}")
        else
            DEVICE_SPECIFIC_OPTION=()
        fi
        readonly DEVICE_SPECIFIC_OPTION

        PATH_OPTION=("-p" "$(pwd)/out/host/linux-x86")
        readonly PATH_OPTION

        if [ "${BLOCK_MODE}" == "true" ]
        then
            BLOCK_OPTION=("--block")
        else
            BLOCK_OPTION=()
        fi
        readonly BLOCK_OPTION
    popd
}


function generate_incr_ota_package(){
    log_info "generate incremental ota package now"

    # when searching ota_scatter.txt, the ota script will assume current working directory is above "out"
    pushd "${OTA_TEMPDIR}"
        cmd=("${OTA_SCRIPT}" "-k" "${RELEASE_KEY}" "${DEVICE_SPECIFIC_OPTION[@]}" "${BLOCK_OPTION[@]}" "${PATH_OPTION[@]}" "-i" "${INCREMENTAL_FROM}" "${INPUT_TARGET_FILE}" "${OUTPUT_OTA_PACKAGE}")
        log_info "execute command now: ${cmd[*]}"
        "${cmd[@]}"
        if [[ "$?" != 0 || ! -f "${OUTPUT_OTA_PACKAGE}" ]]
        then
            log_error "make incremental ota package failed, exit"
            exit 1
        fi
    popd
}


# package update.zip and md5sum to package.zip
function package_md5sum(){
    log_info "package md5sum now"

    echo -n "$(md5sum -b "${OUTPUT_OTA_PACKAGE}" | cut -c1-32)" > "${MD5SUM_FILE_PATH}"
    zip --junk-paths "${PACKAGE_ZIP_FILE_PATH}" "${OUTPUT_OTA_PACKAGE}" "${MD5SUM_FILE_PATH}"
    if [[ "$?" != 0 || ! -s "${PACKAGE_ZIP_FILE_PATH}" ]]
    then
        log_error "package md5sum failed, exit abnormally"
        exit 1
    else
        log_info "package md5sum suceeded: ${PACKAGE_ZIP_FILE_PATH}"
    fi
}

function archive_ota_package(){
    #local path=$(echo "$ARCHIVE_FILE_PATH"|sed 's/\\/\//g')
    local -r FULL_OTA_NAME=${FROM_OTA_NAME}-${TARGET_OTA_NAME}_${ARCHIVE_DATE}
    local -r ARCHIVE_FILE_NAME="package-${FULL_OTA_NAME}.zip"
    local -r ARCHIVE_FILE="$OTA_ARCHIVE_DIR"/"${ARCHIVE_FILE_NAME}"
    log_info "ota archive path is: ${ARCHIVE_FILE}"
    upload_to_unc "${PACKAGE_ZIP_FILE_PATH}" "${ARCHIVE_FILE}"
    if [[ "$?" != 0 ]]
    then
        log_error "archive_ota_package failed, exit abnormally"
        exit 1
    else
        log_info "archive_ota_package succeed : ${ARCHIVE_FILE} "
    fi
}


function print_temp_dir_tree(){
    log_info "tempdir state is as follows:"

    tree -afpsuD "${OTA_TEMPDIR}"
}


function remove_temp_dir(){
    log_info "remove tempdir to reclaim disk space"
    rm -rvf "${OTA_TEMPDIR}"
}


##################
## MAIN FUNCTION #
##################
function main(){
    clean_environment
    parse_arguments "$@"
    get_ota_tools
    unzip_ota_tools
    parse_ota_tools_dir
    generate_incr_ota_package
    package_md5sum
    archive_ota_package
    print_temp_dir_tree
    remove_temp_dir

    log_info "generate incremental ota package successfully"
    exit 0
}


#################################
######  MAIN CALL SECTION  ######
#################################

main "$@"
