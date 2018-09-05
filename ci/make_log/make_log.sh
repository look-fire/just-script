#!/bin/bash


###############################
###### CONSTANTS SECTION ######
###############################
readonly SCRIPTDIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

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

function update(){
    mkdir -p "${CODE_DIR}"
    pushd "${CODE_DIR}"
        rm -rf .* ./*
        #${achivestr}
        repo init -u "${BASE_URL}" -b "${MANIFEST_BRANCH}" -m "${branchName}".xml
        repo sync  -c -j24
        echo "repo sync successful"
        pushd .repo/manifests
            MANIFEST_XML_NAME_FROM=$(find -name "$FROM")
        popd
        pushd .repo/manifests
            MANIFEST_XML_NAME_TARGET=$(find -name "$TARGET")
            Achive=$(find "${ARCHIVE_BASE_DIR}"  -name "$TARGET")
        popd
    popd

}


function parse_options(){  
    find . -maxdepth 1  -name '.repo' | xargs rm -rf

    readonly CODE_DIR="$(myrealpath "code")"
    mkdir -p code
    while [[ $# -gt 1 ]]
    do
        key="$1"
        case "$key" in
            --base-url)
                readonly BASE_URL="$2"
        ;;
            --manifest-branch)
                readonly MANIFEST_BRANCH="$2"
        ;;
            --Branch-name)
                readonly branchName="$2"
        ;;
            --archive-base-dir)
                readonly ARCHIVE_BASE_DIR=$(myrealpath "$2")
                if [ -z "${ARCHIVE_BASE_DIR}" ]
                then
                    log_error2 "archive base directory empty, exit abnormally"
                    abnormal_exit
                fi

                is_safe_path "${ARCHIVE_BASE_DIR}"
                if [ $? != 0 ]
                then
                    log_error2 "archive base directory name not safe: ${ARCHIVE_BASE_DIR}, exit abnormally"
                    abnormal_exit
                fi
        ;;
            --xml-name-from)
                readonly FROM="$2"
                readonly achivebase=$(dirname "$(find "${ARCHIVE_BASE_DIR}" -name "$2")")
                readonly achiverepo="$(grep "repo init" "${achivebase}"/verbose_build.log)"
                readonly achivestr=${achiverepo#*"now:"}
        ;;
            --xml-name-target)
                readonly TARGET="$2"
        ;;
    esac
    shift; shift
    done
}


function init_vars(){
    readonly LOG_FILE="${CODE_DIR}/log_$(date +%Y%m%d%H%M%S).txt"
    rm -f "${LOG_FILE}"
}


function make_log(){
    log_info "GENERATE GIT LOG DIFF NOW"
    pushd "${CODE_DIR}"
        GIT_LOG_DIFF_TOBE_ARCHIVED=$(myrealpath "${LOG_FILE}")
        local -r LOGFILE_TEMP=$(myrealpath 'log_cm')
        rm -f "${GIT_LOG_DIFF_TOBE_ARCHIVED}" "${LOGFILE_TEMP}"
        touch "${GIT_LOG_DIFF_TOBE_ARCHIVED}" "${LOGFILE_TEMP}"

        repo diffmanifests "${MANIFEST_XML_NAME_FROM}" "${MANIFEST_XML_NAME_TARGET}" | awk '{if($3~/^from$/ && $2~/^changed$/ && $5~/^to$/ || $3~/^revision$/ && $2~/^at$/)print}' | awk '{print $1,$4,$6}' > "${LOGFILE_TEMP}"
        if [ "${PIPESTATUS[0]}" != 0 ]
        then
            log_error2 "repo diff manifests failed"
        fi

        sed -i 's/refs\/tags\///g' "${LOGFILE_TEMP}"

        local PROJECT_PATH
        local CHANGE_FROM_REVISION
        local CHANGE_TO_REVISION
        while read -r line
        do
            PROJECT_PATH=$(echo "$line" | awk  '{print $1}')
            CHANGE_FROM_REVISION=$(echo "$line" | awk  '{print $2}')
            CHANGE_TO_REVISION=$(echo "$line" | awk  '{print $3}')
            log_info "PROJECT_PATH: ${PROJECT_PATH}"
            log_info "CHANGE_FROM_REVISION: ${CHANGE_FROM_REVISION}"
            log_info "CHANGE_TO_REVISION: ${CHANGE_TO_REVISION}"
            if [ -d "${PROJECT_PATH}" ]
            then
                pushd "${PROJECT_PATH}"
                    if [ ! -n "${CHANGE_TO_REVISION}" ];then
                        echo "${PROJECT_PATH}" >> "${GIT_LOG_DIFF_TOBE_ARCHIVED}"
                        git log  "${CHANGE_FROM_REVISION}" --pretty="%an|[%h] %s" | grep -v "Merge" | awk -F\| '{printf("%-15s\t%s\n",$1, $2) }' >> "${GIT_LOG_DIFF_TOBE_ARCHIVED}"
                    else
                        echo "${PROJECT_PATH}" >> "${GIT_LOG_DIFF_TOBE_ARCHIVED}"
                        git log  "${CHANGE_FROM_REVISION}..${CHANGE_TO_REVISION}" --pretty="%an|[%h] %s" | grep -v "Merge" | awk -F\| '{printf("%-15s\t%s\n",$1, $2) }' >> "${GIT_LOG_DIFF_TOBE_ARCHIVED}"
                        if [ "${PIPESTATUS[0]}" -ne 0 ];then
                            git log "${CHANGE_TO_REVISION}" --pretty="%an|[%h] %s" | grep -v "Merge" | awk -F\| '{printf("%-15s\t%s\n",$1, $2) }' >> "${GIT_LOG_DIFF_TOBE_ARCHIVED}"
                        fi
                    fi
                popd
            else
                log_warning "${PROJECT_PATH} does not exist, do not get git log diff"
            fi
        done < "${LOGFILE_TEMP}"
    popd

}


function achive(){
    if [ ! -e "${LOG_FILE}" ]
    then
        log_error2 "failed to find LOG_FILE"
    fi
    cp "${LOG_FILE}" "$(dirname "${Achive}")"
}


##################
## MAIN FUNCTION #
##################
function main(){
    parse_options "$@"
    init_vars
    update
    make_log
   # achive
}


#################################
######  MAIN CALL SECTION  ######
#################################

main "$@"

