#!/bin/bash
#Transsion Top Secret
#  archive_to_cifs.sh: archive local files to remote cifs directory
#  ONLY SUPPORT CIFS allinfo/mkdir/put OPERATION, FORBID ANY OTHER DANGEROUS OPERATION
#  WARNING: DO NOT PRINT PASSWORD ANYWHERE IN THIS SCRIPT


###############################
###### CONSTANTS SECTION ######
###############################
# passed by environment variable, DO NOT UNSET
declare SMB_USER
declare SMB_PASSWD

readonly SCRIPTDIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
readonly OPTION_VAR_ARRAY=(
    SERVER
    SERVICE
    LOCAL_DIR
    DEST_DIR
    ARCHIVE_DIR_NAME
)
readonly STATUS_ARGUMENT_ERROR=111
readonly STATUS_DESTDIR_NOT_EXIST=112
readonly STATUS_MKDIR_FAILED=113
readonly STATUS_PUT_FILE_FAILED=114
readonly STATUS_FILE_CONFIDENTIAL=115


########################################
###### FUNCTION DECLARATION SECTION  ###
########################################
# shellcheck disable=SC1090
source "${SCRIPTDIR}"/commonlibs.sh
if [ "$?" != 0 ]
then
    echo "commonslibs.sh DOES NOT EXIST, EXIT ABNORMALLY"
    exit 1
fi


function parse_options(){
    # NOTICE: try out best to transform directory paths to absolute paths(e.g. './' -> '/home/user/mycode')
    while [[ $# -gt 1 ]]
    do
        key="$1"

        case "$key" in
            --server)
                readonly SERVER="$2"
                is_safe_name_component "${SERVER}"
                if [ $? != 0 ]
                then
                    echo "server name not safe: ${SERVER}, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                ;;
            --service)
                readonly SERVICE="$2"
                is_safe_name_component "${SERVICE}"
                if [ $? != 0 ]
                then
                    echo "service name not safe: ${SERVICE}, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                ;;
            --local-dir)
                if [ -z "$2" ]
                then
                    echo "no local directory designated, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                readonly LOCAL_DIR=$(myrealpath "$2")

                if [ ! -d "${LOCAL_DIR}" ]
                then
                    echo "path does not exist: ${LOCAL_DIR}, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi

                if [ -z "$(ls -A "${LOCAL_DIR}")" ]
                then
                    echo "empty local dir: ${LOCAL_DIR}, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi

                is_safe_path "${LOCAL_DIR}"
                if [ $? != 0 ]
                then
                    echo "path not safe: ${LOCAL_DIR}, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                ;;
            --dest-dir)    # like "Z1\A1_BOM\MP" or "Z1/A1_BOM/MP"
                readonly DEST_DIR=$(echo "$2"|sed 's/\//\\/g')
                if [ -z "${DEST_DIR}" ]
                then
                    echo "no dest dir designated, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                is_safe_utf8_windows_path "${DEST_DIR}"
                if [ $? != 0 ]
                then
                    echo "path not safe: ${DEST_DIR}, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                ;;
            --archive-dir-name)
                readonly ARCHIVE_DIR_NAME="$2"
                if [ -z "${ARCHIVE_DIR_NAME}" ]
                then
                    echo "no archive directory name designated, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                is_safe_name_component "${ARCHIVE_DIR_NAME}"
                if [ $? != 0 ]
                then
                    echo "path not safe: ${ARCHIVE_DIR_NAME}, exit abnormally"
                    exit "$STATUS_ARGUMENT_ERROR"
                fi
                ;;
            *)
                log_error "do not allow non-option command line arguments: $1, exit abnormally"
                exit "$STATUS_ARGUMENT_ERROR"
                ;;
        esac
        shift; shift # past option, do not support regular argument
    done

    if [[ -z "${SMB_USER+x}" || -z "${SMB_PASSWD+x}" ]]
    then
        log_error "SMB_USER or SMB_PASSWD not set, must be given through environment variables, exit abnormally"
        exit "$STATUS_ARGUMENT_ERROR"
    fi

    # ensure all option variables are initialized
    for myvar in "${OPTION_VAR_ARRAY[@]}"
    do
        if [ -z "${myvar+x}" ]
        then
           log_error "${myvar} not set, must be given through command line, exit abnormally"
           exit "$STATUS_ARGUMENT_ERROR"
        fi
    done
}


function init_vars(){
    readonly SERVICE_NAME="//${SERVER}/${SERVICE}"
}


function check_local_dir(){
    # information security check
    pushd "${LOCAL_DIR}"
        for file in *
        do
            is_file_confidential "${file}"
            if [ "$?" == 0 ]
            then
                log_error "file ${file} is confidential, must not upload, exit abnormally"
                exit "$STATUS_FILE_CONFIDENTIAL"
            fi
        done
    popd
}


function execute_smbcmd(){
    # dest dir existence check
    local -r smbcmd="$1"
    local basecmd
    local output

    basecmd=(smbclient "${SERVICE_NAME}" "-c" "${smbcmd}")

    log_info "execute cmd now: ${basecmd[*]}"

    output=$("${basecmd[@]}" -A=<(echo -e "username = ${SMB_USER}\npassword = ${SMB_PASSWD}"))
    executestatus=$?

    if [[ "${executestatus}" != 0 || "${output}" =~ "NT_STATUS_" ||  "${output}" =~ "command not found" ]]
    then
        log_error "execute cmd failed: ${basecmd[*]} , output: ${output}"
        return 1
    fi

    return 0
}

# NOTICE:
#     from https://www.samba.org/samba/docs/man/manpages/smbclient.1.html
#         You can specify file names which have spaces in them by quoting the name with double quotes, for example "a long file name".
function check_dest_dir(){
    # dest dir existence check
    execute_smbcmd "allinfo \"${DEST_DIR}\""
    if [ "$?" != 0 ]
    then
        exit "$STATUS_DESTDIR_NOT_EXIST"
    fi
}

function make_archive_dir(){
    # dest dir existence check
    execute_smbcmd "mkdir \"${DEST_DIR}\\${ARCHIVE_DIR_NAME}\""
    if [ "$?" != 0 ]
    then
        exit "$STATUS_MKDIR_FAILED"
    fi
}

function put_file(){
    local -r localfile="$1"
    local -r remotefilename="$2"
    execute_smbcmd "put \"${localfile}\" \"${DEST_DIR}\\${ARCHIVE_DIR_NAME}\\${remotefilename}\""
    if [ "$?" != 0 ]
    then
        exit "$STATUS_PUT_FILE_FAILED"
    fi
}

function put_files(){
    # check confidential files again to avoid race condition
    pushd "${LOCAL_DIR}"
        for file in *
        do
            is_file_confidential "${file}"
            if [ "$?" == 0 ]
            then
                log_error "file ${file} is confidential, must not upload, exit abnormally"
                exit "$STATUS_FILE_CONFIDENTIAL"
            fi
            put_file "${file}" "${file}"
        done
    popd
}


##################
## MAIN FUNCTION #
##################
function main(){
    parse_options "$@"
    init_vars
    check_local_dir
    check_dest_dir
    make_archive_dir
    put_files
}


#################################
######  MAIN CALL SECTION  ######
#################################
main "$@"

