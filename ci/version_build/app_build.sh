#!/bin/bash
#Transsion Top Secret


###############################
###### CONSTANTS SECTION ######
###############################
# passed by environment variable, DO NOT UNSET
declare SMB_USER
declare SMB_PASSWD
declare APK_PATH

readonly SCRIPTDIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
readonly BUILD_OUTPUTS_RELATIVE_DIR="app/build/outputs"
readonly DATE=$(date +%Y%m%d%H%M%S)
readonly DOT_DATE=$(date +%Y.%m.%d)
readonly OPTION_VAR_ARRAY=(
    SERVER
    SERVICE
    DEST_DIR
    APP_NAME
    GIT_PROJECT
    DEBUG_MODE
    GP
    XSHARE_HACK
    ANDROID_MANIFEST
    CUSTOM_APK_PATH
    CUSTOM_MAPPING_PATH
    BUILD_OPTION
)


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


# prevent environment variable pollution
function clean_environment(){
    for myvar in "${OPTION_VAR_ARRAY[@]}"
    do
        unset "$myvar"
    done
}


function parse_options(){
    # NOTICE: try out best to transform directory paths to absolute paths(e.g. './' -> '/home/user/mycode')
    while [[ $# -gt 1 ]]
    do
        key="$1"

        case "$key" in
            --xshare-hack)
                readonly XSHARE_HACK="$2"
                all_switch "${XSHARE_HACK}"
                if [ "$?" != 0 ]
                then
                    log_error "--xshare-hack should be true or false, exit abnormally"
                    exit 1
                fi
                ;;
            --app-name)
                readonly APP_NAME="$2"
                is_safe_name_component "${APP_NAME}"
                if [ $? != 0 ]
                then
                    log_error "app name not safe: ${APP_NAME}, exit abnormally"
                    exit 1
                fi
                ;;
            --server)
                readonly SERVER="$2"
                is_safe_name_component "${SERVER}"
                if [ $? != 0 ]
                then
                    log_error "server name not safe: ${SERVER}, exit abnormally"
                    exit 1
                fi
                ;;
            --service)
                readonly SERVICE="$2"
                is_safe_name_component "${SERVICE}"
                if [ $? != 0 ]
                then
                    log_error "service name not safe: ${SERVICE}, exit abnormally"
                    exit 1
                fi
                ;;
            --dest-dir)    # like "Z1\A1_BOM\MP" or "Z1/A1_BOM/MP"
                if [ -z "${XSHARE_HACK+x}" ]
                then
                    log_error "please set --xshare-hack before --dest-dir, exit abnormally"
                    exit 1
                fi

                if [ -z "${GP+x}" ]
                then
                    log_error "please set --gp before --dest-dir, exit abnormally"
                    exit 1
                fi

                DEST_DIR=$(echo "$2"|sed 's/\//\\/g')
                if [ -z "${DEST_DIR}" ]
                then
                    log_error "no dest dir designated, exit abnormally"
                    exit 1
                fi

                if [ "${XSHARE_HACK}" == false ]
                then
                    log_info "It is normal apk"
                    if [ "${GP}" == true ]
                    then
                        log_info "In GP mode"
                        DEST_DIR="${DEST_DIR}\\GP上架正式版本"
                    else
                        log_info "Not in GP mode"
                        DEST_DIR="${DEST_DIR}\\内测版本"
                    fi
                else
                    log_info "It is XSHARE apk"
                fi
                readonly DEST_DIR
                log_info "archive path: ${DEST_DIR}"

                is_safe_utf8_windows_path "${DEST_DIR}"
                if [ $? != 0 ]
                then
                    log_error "path not safe: ${DEST_DIR}, exit abnormally"
                    exit 1
                fi
                ;;
            --git-project)
                readonly GIT_PROJECT="$2"
                is_safe_path "${GIT_PROJECT}"
                if [ $? != 0 ]
                then
                    log_error "git project name not safe: ${GIT_PROJECT}, exit abnormally"
                    exit 1
                fi
                ;;
            --git-branch)
                readonly GIT_BRANCH="$2"
                is_safe_name_component "${GIT_BRANCH}"
                if [ $? != 0 ]
                then
                    log_error "git branch name not safe: ${GIT_BRANCH}, exit abnormally"
                    exit 1
                fi
                ;;
            --gerrit-ip)
                readonly GERRIT_IP="$2"
                is_safe_name_component "${GERRIT_IP}"  # simple but not precise
                if [ $? != 0 ]
                then
                    log_error "gerrit ip not safe: ${GERRIT_IP}, exit abnormally"
                    exit 1
                fi
                ;;
            --gp)
                readonly GP="$2"
                all_switch "${GP}"
                if [ "$?" != 0 ]
                then
                    log_error "--gp should be true or false, exit abnormally"
                    exit 1
                fi
                ;;
            --android-manifest)
                readonly ANDROID_MANIFEST="$2"
                if [ -n "${ANDROID_MANIFEST}" ]
                then
                    is_safe_path "${ANDROID_MANIFEST}"
                    if [ $? != 0 ]
                    then
                        log_error "android manifest not safe: ${ANDROID_MANIFEST}, exit abnormally"
                        exit 1
                    fi
                fi
                ;;
            --custom-apk-path)
                # may be glob path, containing '*'
                readonly CUSTOM_APK_PATH="$2"
                if [ -n "${CUSTOM_APK_PATH}" ]
                then
                    is_safe_glob_path "${CUSTOM_APK_PATH}"
                    if [ $? != 0 ]
                    then
                        log_error "custom apk path not safe: ${CUSTOM_APK_PATH}, exit abnormally"
                        exit 1
                    fi
                fi
                ;;
            --custom-mapping-path)
                readonly CUSTOM_MAPPING_PATH="$2"
                if [ -n "${CUSTOM_MAPPING_PATH}" ]
                then
                    is_safe_path "${CUSTOM_MAPPING_PATH}"
                    if [ $? != 0 ]
                    then
                        log_error "custom mapping path not safe: ${CUSTOM_MAPPING_PATH}, exit abnormally"
                        exit 1
                    fi
                fi
                ;;
            --build-option)
                readonly BUILD_OPTION="$2"
                ;;
            --debug-mode)
                readonly DEBUG_MODE="$2"
                all_switch "${DEBUG_MODE}"
                if [ "$?" != 0 ]
                then
                    log_error "--debug-mode should be true or false, exit abnormally"
                    exit 1
                fi
                ;;
            *)
                log_error "do not allow non-option command line arguments: $1, exit abnormally"
                exit 1
                ;;
        esac
        shift; shift # past option, do not support regular argument
    done

    if [[ -z "${SMB_USER+x}" || -z "${SMB_PASSWD+x}" ]]
    then
        log_error "SMB_USER or SMB_PASSWD not set, must be given through environment variables, exit abnormally"
        exit 1
    fi

    # ensure all option variables are initialized
    for myvar in "${OPTION_VAR_ARRAY[@]}"
    do
        eval "[ -z \${${myvar}+x} ]"
        if [ "$?" == 0 ]
        then
           log_error "${myvar} not set, must be given through command line, exit abnormally"
           exit 1
        fi
    done
}


function clone_app(){
    pushd "${CODE_DIR}"
        local -r clonecmd=("git" "clone" "ssh://${GERRIT_IP}:29418/${GIT_PROJECT}" "-b" "${GIT_BRANCH}")
        log_info "execute cmd now: ${clonecmd[*]}"
        "${clonecmd[@]}"
        if [ $? != 0 ]
        then
            log_error "git clone app failed, exit abnormally"
            exit 1
        fi
    popd
}


function exit_if_built_before(){
    if [ "${GP}" == "true" ]
    then
        log_info "build in GP mode, always build, ingore whether current commit was built before"
        return 0
    fi

    pushd "${CODE_DIR}/${GIT_PROJECT}"
        local -r head_tags=$(git tag --contains HEAD|grep "${APP_NAME}")
        if [ -n "${head_tags}" ]
        then
            log_info "the HEAD contains build tag: ${head_tags}, do not build any more, exit normally"
            exit 0
        fi
    popd
}


function build_app(){
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        log_info "execute: ${BUILD_CMD[*]}"
        "${BUILD_CMD[@]}"
        if [ $? != 0 ]
        then
            log_error "execute gradlew failed, exit abnormally"
            exit 1
        fi

        # determine output apk path
        if [ -n "${CUSTOM_APK_PATH}" ]
        then
            # shellcheck disable=SC2086
            local CUSTOM_APK_PATHS=($(ls ${CUSTOM_APK_PATH}))
            if [ "${#CUSTOM_APK_PATHS[@]}" != 1 ]
            then
                log_error "no apk generated, exit abnormally"
                exit 1
            else
                APK_PATH=${CUSTOM_APK_PATHS[0]}
                readonly APK_PATH
            fi
        else
            APK_PATH="${BUILD_OUTPUTS_ABSOLUTE_DIR}"/apk/app-release.apk
            readonly APK_PATH

            ls "${APK_PATH}" 1>/dev/null 2>&1
            if [ $? != 0 ]
            then
                log_error "no apk generated, exit abnormally"
                exit 1
            fi
        fi
    popd
}


function generate_release_note(){
    # NOTICE: "REMOTE_ARCHIVE_DIR_NAME" is not stable
    local -r out_dir="$(myrealpath "$1")"
    echo "项目名: ${GIT_PROJECT}
原始版本库路径: ssh://${GERRIT_IP}:29418/${GIT_PROJECT}
branch: ${GIT_BRANCH}
快照(Tag): ${BUILD_TAG_NAME}
路径: \\\\${SERVER}\\${SERVICE}\\${DEST_DIR}\\${REMOTE_ARCHIVE_DIR_NAME}
编译命令: ${BUILD_CMD[*]}
版本名: ${VERSION_NAME}
版本号: ${VERSION_CODE}
修改内容:
" > "${out_dir}/release_note.txt"
}


function generate_local_archive(){
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        local -r LOCAL_ARCHIVE_DIR="$(myrealpath "$1")"

        log_info "apk to be archived: ${APK_PATH}"
        cp "${APK_PATH}" "${LOCAL_ARCHIVE_DIR}/${ARCHIVE_APK_NAME}"
        if [ "$?" != 0 ]
        then
            log_error "apk not found, exit abnormally"
            exit 1
        fi

        if [ -n "${CUSTOM_MAPPING_PATH}" ]
        then
            cp "${CUSTOM_MAPPING_PATH}" "${LOCAL_ARCHIVE_DIR}"
        else
            cp "${BUILD_OUTPUTS_ABSOLUTE_DIR}"/mapping/release/mapping.txt "${LOCAL_ARCHIVE_DIR}"
        fi

        git rev-parse HEAD > "${LOCAL_ARCHIVE_DIR}/HEAD_COMMIT.txt"
        pushd "${LOCAL_ARCHIVE_DIR}"
            # do not reflect relative path in md5 sum file
            md5sum "${ARCHIVE_APK_NAME}" > "${ARCHIVE_APK_NAME}.md5sum.txt"
        popd
        generate_release_note "${LOCAL_ARCHIVE_DIR}"

        cp "${SECRET_TAG}" "${LOCAL_ARCHIVE_DIR}"
    popd
}


function tag_local_code(){
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        # tag to indicate HEAD has been built
        log_info "execute cmd now: ${TAG_CMD[*]}"
        "${TAG_CMD[@]}"
        if [ "$?" != 0 ]
        then
            log_error "failed to git tag code, exit abnormally"
            exit 1
        fi

    popd
}


function dry_run_push_tag(){
    log_info "dry run push tag, to prevent push failure after build or archive"
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        log_info "execute cmd now: ${DRYRUN_PUSH_TAG_CMD[*]}"
        "${DRYRUN_PUSH_TAG_CMD[@]}"
        if [ "$?" != 0 ]
        then
            log_error "failed to dry run push tag, exit abnormally"
            exit 1
        fi
    popd
}


function push_commit_and_tag(){
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        log_info "execute cmd now: ${COMMIT_PUSH_CMD[*]}"
        "${COMMIT_PUSH_CMD[@]}"
        if [ "$?" != 0 ]
        then
            log_error "failed to git push commit, exit abnormally"
            exit 1
        fi

        log_info "execute cmd now: ${PUSH_TAG_CMD[*]}"
        "${PUSH_TAG_CMD[@]}"
        if [ "$?" != 0 ]
        then
            log_error "failed to push tag, exit abnormally"
            exit 1
        fi
    popd
}


function archive_app(){
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        # make local temp archive dir
        local -r LOCAL_ARCHIVE_DIR="$(myrealpath temp_archive)"
        rm -rf "${LOCAL_ARCHIVE_DIR}"
        mkdir "${LOCAL_ARCHIVE_DIR}"

        # determine a remote archive dir name
        local REMOTE_ARCHIVE_DIR_NAME=${DOT_DATE}
        if [ "${DEBUG_MODE}" == true ]
        then
            local -r DEBUG_SUFFIX="_CI_DEBUG"
        fi
        REMOTE_ARCHIVE_DIR_NAME="${REMOTE_ARCHIVE_DIR_NAME}${DEBUG_SUFFIX}"

        # archive locally
        generate_local_archive "${LOCAL_ARCHIVE_DIR}"

        # try remote archive
        "$SCRIPTDIR"/archive_to_cifs.sh --server "$SERVER" --service "$SERVICE" --local-dir "${LOCAL_ARCHIVE_DIR}" --dest-dir "$DEST_DIR" --archive-dir-name "${REMOTE_ARCHIVE_DIR_NAME}"
        local status=$?
        if [ "${status}" == 0 ]
        then
            log_info "archive successfully"
        elif [ "${status}" == "112" ]
        then
            log_error "failed to archive, dest dir does not exist: $DEST_DIR, exit abnormally"
            exit 1
        elif [ "${status}" == "113" ]
        then
            log_info "make dir failed, try another dir name"
            # try another remote archive dir name
            REMOTE_ARCHIVE_DIR_NAME="${REMOTE_ARCHIVE_DIR_NAME}_$(date +%H%M%S)"
            generate_release_note "${LOCAL_ARCHIVE_DIR}"  # reflect new  REMOTE_ARCHIVE_DIR_NAME in release note
            "$SCRIPTDIR"/archive_to_cifs.sh --server "$SERVER" --service "$SERVICE" --local-dir "${LOCAL_ARCHIVE_DIR}" --dest-dir "$DEST_DIR" --archive-dir-name "${REMOTE_ARCHIVE_DIR_NAME}"
            if [ "$?" != 0 ]
            then
                log_error "failed to archive, exit abnormally"
                exit 1
            fi
        else
            log_error "failed to archive, exit abnormally"
            exit 1
        fi
    popd
}


function init_basic_vars(){
    readonly CODE_DIR=$(myrealpath "code")
    rm -rf "${CODE_DIR}"
    mkdir -p "${CODE_DIR}"

    if [ -n "${BUILD_OPTION}" ]
    then
        BUILD_CMD=("bash" "gradlew" ${BUILD_OPTION})
    else
        BUILD_CMD=("bash" "gradlew" "build")
    fi
    readonly BUILD_CMD

    # default build outputs dir
    readonly BUILD_OUTPUTS_ABSOLUTE_DIR="${CODE_DIR}/${GIT_PROJECT}/${BUILD_OUTPUTS_RELATIVE_DIR}"

    # secret tag
    readonly SECRET_TAG="${SCRIPTDIR}/secret_tag/内部公开-InternalUse.pdf"

    declare -a DRYRUN_COMMIT_PUSH_CMD
    declare -a COMMIT_PUSH_CMD
    declare -a DRYRUN_PUSH_TAG_CMD
    declare -a PUSH_TAG_CMD
    declare -a TAG_CMD
}


function commit_local_code_version(){
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        git pull --rebase

        if [ -n "${ANDROID_MANIFEST}" ]
        then
            if [ ! -f "${ANDROID_MANIFEST}" ]
            then
                log_error "android manifest does not exist in code tree: ${ANDROID_MANIFEST}, exit abnormally"
                exit 1
            fi

            readonly VERSION_NAME_LITERAL="android:versionName"
            readonly VERSION_CODE_LITERAL="android:versionCode"
            readonly VERSION_CONFIG_FILE="${ANDROID_MANIFEST}"
        else
            readonly VERSION_NAME_LITERAL="versionName"
            readonly VERSION_CODE_LITERAL="versionCode"
            readonly VERSION_CONFIG_FILE="app/build.gradle"
        fi

        local -r original_version_name=$(grep "${VERSION_NAME_LITERAL}" "${VERSION_CONFIG_FILE}" |grep -aoE '[0-9\.]+'|head -1)
        local -r original_version_code=$(grep "${VERSION_CODE_LITERAL}" "${VERSION_CONFIG_FILE}" |grep -aoE '[0-9]+'|head -1)

        local -r version_name_field1=$(echo "${original_version_name}"|cut -d '.' -f1)
        local -r version_name_field2=$(echo "${original_version_name}"|cut -d '.' -f2)
        local -r version_name_field3=$(echo "${original_version_name}"|cut -d '.' -f3)
        local -r version_name_field4=$(echo "${original_version_name}"|cut -d '.' -f4)

        log_info "original version code: ${original_version_code}"
        log_info "original version name field1: ${version_name_field1} field2: ${version_name_field2} field3: ${version_name_field3} field4: ${version_name_field4}"

        local -r new_code=$((original_version_code+1))

        # determine new version name
        if [ "${XSHARE_HACK}" == false ]
        then
            # normal rule
            local -r version_name_field3_basic=$(echo "${version_name_field3}"|grep -aoE '^[0-9\.]+')
            local version_name_field3_basic_increment
            if [ "${#version_name_field3_basic}" == 3 ]
            then
                # shellcheck disable=SC2001
                local -r version_name_field3_basic_no_leading_zeros=$(echo "${version_name_field3_basic}"| sed 's/^0*//')
                local -r version_name_field3_basic_no_leading_zeros_plus1=$((version_name_field3_basic_no_leading_zeros+1))
                printf -v version_name_field3_basic_increment '%03d' ${version_name_field3_basic_no_leading_zeros_plus1}
            else
                version_name_field3_basic_increment=$((version_name_field3_basic+1))
            fi

            local -r new_name=${version_name_field1}.${version_name_field2}.${version_name_field3_basic_increment}.${version_name_field4}
        else
            # XSHARE rule
            if [ "${GP}" == true ]
            then
                local -r version_name_field3_plus1=$((version_name_field3+1))
                local -r new_name=${version_name_field1}.${version_name_field2}.${version_name_field3_plus1}
            else
                local -r version_name_field4_plus1=$((version_name_field4+1))
                local -r new_name=${version_name_field1}.${version_name_field2}.${version_name_field3}.${version_name_field4_plus1}
            fi

        fi

        sed -i -E "s/(${VERSION_NAME_LITERAL}.*)${original_version_name}(.*)$/\1${new_name}\2/g" "${VERSION_CONFIG_FILE}"
        sed -i -E "s/(${VERSION_CODE_LITERAL}.*)${original_version_code}(.*)$/\1${new_code}\2/g" "${VERSION_CONFIG_FILE}"

        git add "${VERSION_CONFIG_FILE}"
        git commit -m "change version name and version code"
        if [ $? != 0 ]
        then
            log_error "failed to change version name and version code, exit abnormally"
            exit 1
        fi
    popd
}


function dry_run_push_commit(){
    log_info "dry run push commit, with modified version name and code, to prevent push failure after build or archive"
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        log_info "execute cmd now: ${DRYRUN_COMMIT_PUSH_CMD[*]}"
        "${DRYRUN_COMMIT_PUSH_CMD[@]}"
        if [ $? != 0 ]
        then
            log_error "failed to dry run push commit, exit abnormally"
            exit 1
        fi
    popd
}


function init_basic_vars_from_code(){
    pushd "${CODE_DIR}/${GIT_PROJECT}"
        readonly VERSION_NAME=$(grep "${VERSION_NAME_LITERAL}" "${VERSION_CONFIG_FILE}" |grep -aoE '[0-9\.]+'|head -1)
        readonly VERSION_CODE=$(grep "${VERSION_CODE_LITERAL}" "${VERSION_CONFIG_FILE}" |grep -aoE '[0-9]+'|head -1)

        readonly ARCHIVE_APK_NAME="${APP_NAME}_V${VERSION_NAME}_${DATE}.apk"
        readonly BUILD_TAG_NAME="${APP_NAME}_${VERSION_NAME}_${DATE}"

        readonly PROJECT_REMOTE_BRANCH=$(git config branch."${GIT_BRANCH}".merge)
        TAG_CMD=("git" "tag" "-a" "${BUILD_TAG_NAME}" "-m" "tag after build: ${BUILD_TAG_NAME}")
        DRYRUN_COMMIT_PUSH_CMD=("git" "push" "--dry-run" "$(git remote)" "HEAD:${PROJECT_REMOTE_BRANCH}")
        DRYRUN_PUSH_TAG_CMD=("git" "push" "--dry-run" "$(git remote)" "${BUILD_TAG_NAME}")
        if [ "${DEBUG_MODE}" == true ]
        then
            COMMIT_PUSH_CMD=( "${DRYRUN_COMMIT_PUSH_CMD[@]}" )
            PUSH_TAG_CMD=( "${DRYRUN_PUSH_TAG_CMD[@]}" )
        else
            COMMIT_PUSH_CMD=("git" "push" "$(git remote)" "HEAD:${PROJECT_REMOTE_BRANCH}")
            PUSH_TAG_CMD=("git" "push" "$(git remote)" "${BUILD_TAG_NAME}")
        fi
    popd
}


##################
## MAIN FUNCTION #
##################
function main(){
    clean_environment
    parse_options "$@"

    init_basic_vars

    clone_app

    exit_if_built_before
    commit_local_code_version
    init_basic_vars_from_code
    dry_run_push_commit

    build_app

    tag_local_code
    dry_run_push_tag

    archive_app

    # push commit and tag after remote archive, in case commit is tagged already built but not archived yet
    push_commit_and_tag
}


#################################
######  MAIN CALL SECTION  ######
#################################

main "$@"
