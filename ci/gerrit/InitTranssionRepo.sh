#!/bin/bash
#Transsion Top Secret

# Init Transsion Repo
# usage eg: ./${0} 192.168.10.40 \\192.168.1.75\test2\平台研发部\王伟槐\MT6737T_Androin_N project.list
readonly GERRIT_SERVER_IP="${1}"
readonly MTK_BASE_CODE="$2"
readonly ORG_PRO_LIST="$3"
readonly PATHROOT=$(pwd)

function mk_dir()
{
	if [ -d "${1}" ]
	then
		rm -rf "${1}"
		mkdir -p "${1}" || exit 1
	else
		mkdir -p "${1}" || exit 1
	fi
}

function log(){
    local -r MODE="${1}"
    shift
    echo "$(date '+%Y-%m-%d %H:%M:%S') ${MODE}: $*"
}

function log_error(){
    # NOTICE: when calling log_error, the build process should be regarded as failure
    log "ERROR" "$@"
}

function compare_pro_list()
{
    cd "${PATHROOT}"/InitRepo/MTK_CODE_BASE/alps/
    for i in $(cat "${PATHROOT}"/ORG_PRO_LIST)
    do
	local git_par_dir=`dirname #{i#*/}`
	for j in `find ${git_par_dir} -maxdepth 1 -type d`
	do
		grep ${j} "${PATHROOT}"/ORG_PRO_LIST
		if [ ${PIPESTATUS} -ne 0 ]
		then
			echo "`dirname $i`/`basename $j`" >> "${PATHROOT}"/ORG_PRO_LIST
		fi
	done
    done
    cd -
}

function create_repos()
{
	mk_dir "${PATHROOT}"/InitRepo/git_repo
	mv "${PATHROOT}"/ORG_PRO_LIST "${PATHROOT}"/InitRepo/git_repo
	cd "${PATHROOT}"/InitRepo/git_repo || exit 1
	MANIFEST_PRO=$(grep manifest ORG_PRO_LIST)
	if [ -z "${MANIFEST_PRO}" ]
	then
		echo "pls add manifest repository to ${ORG_PRO_LIST}"
		PLATFORM=$(sed -n '1p' ORG_PRO_LIST | awk -F'/' '{print $1}')
		echo "${PLATFORM}/manifest" >> ORG_PRO_LIST
	fi
	for i in $(cat ORG_PRO_LIST)
	do
		echo "${i}"
		ssh -p 29418 "${GERRIT_SERVER_IP}" gerrit create-project "${i}" --empty-commit -b import -t FAST_FORWARD_ONLY -p All-Projects
	done
	git clone ssh://"${GERRIT_SERVER_IP}":29418/"${MANIFEST_PRO}" -b import
	cp ORG_PRO_LIST manifest/
	cd manifest || exit 1
	for i in $(cat ORG_PRO_LIST)
	do
		echo "  <project name=\"${i}\" path=\"${i#*/}\" />" >> "${BASELINE_NAME}".xml
	done
	sed "1 i<manifest>\n  <remote fetch=\"ssh:\/\/${GERRIT_SERVER_IP}:29418\" name=\"origin\" review=\"http:\/\/${GERRIT_SERVER_IP}:80\"\/>\n  <default remote=\"origin\" revision=\"import\"/>" -i "${BASELINE_NAME}".xml
	sed '$ a<\/manifest>' -i "${BASELINE_NAME}".xml
	sed '1 i<?xml version=\"1.0\" encoding=\"UTF-8\"?>' -i "${BASELINE_NAME}".xml
	git add "${BASELINE_NAME}".xml
	git commit -m "Init ${BASELINE_NAME} source manifest.xml"
	git push origin import
	cd ..
	rm -rf manifest
	
	repo init -u ssh://"${GERRIT_SERVER_IP}":29418/"${MANIFEST_PRO}" -b import -m "${BASELINE_NAME}".xml
	repo sync -cj4
	repo start import --all
	repo forall -c git tag -a emptycommit -m "emptycommit"
	repo forall -c git push origin emptycommit
}
function deal_with_org_code()
{
	MNT_DIR=$(echo "${MTK_BASE_CODE}" | sed 's/\\/\//g' |sed 's/192.168.1.75/mnt/')
	mk_dir "${PATHROOT}"/InitRepo/MTK_CODE_BASE
	cp "${MNT_DIR}"/* "${PATHROOT}"/InitRepo/MTK_CODE_BASE/ -rf
	cd "${PATHROOT}"/InitRepo/MTK_CODE_BASE || exit 1
	BASELINE_NAME=$(find . -maxdepth 1 -type f -name "*.md5" -exec basename {} \; | sed 's/\.md5//g')
	md5sum -c "${BASELINE_NAME}".md5 ||  exit 1
	tar -zxvf ALPS*.tar.gz
	cat "${BASELINE_NAME}"_INHOUSE.tar.gz* | tar zxf -
	find alps -name ".gitignore" -name ".git" -exec rm -rf {} \;
}

function upload_code()
{
	cp "${PATHROOT}"/InitRepo/MTK_CODE_BASE/alps/* "${PATHROOT}"/InitRepo/git_repo/ -a
	cd "${PATHROOT}"/InitRepo/git_repo/ || exit 1
	find . -type d -empty -exec touch {}/.gitignore \;
	cp $(find . -maxdepth 1 -type f) build/
	sed -i '/path="build"/s/\/>/>/g' .repo/manifest.xml
	sed -i '/path="build"/a\  </project>' .repo/manifest.xml
	for i in $(find . -maxdepth 1 -type f -exec basename {} \; | tac)
	do
		sed -i "/path=\"build\"/a\\\t<copyfile dest=\"${i}\" src=\"${i}\"/>" .repo/manifest.xml
	done
	cp $(find frameworks/base -maxdepth 1 -type f ! -name Android.mk) frameworks/base/api
	cp $(find frameworks/base -maxdepth 1 -type f -name Android.mk)	frameworks/base/api/root.mk
	sed -i '/path="frameworks\/base\/api"/s/\/>/>/g' .repo/manifest.xml
        sed -i '/path="frameworks\/base\/api"/a\  </project>' .repo/manifest.xml
        for i in $(find frameworks/base -maxdepth 1 -type f ! -name Android.mk -exec basename {} \; | tac)
        do
        	sed -i "/path=\"frameworks\/base\/api\"/a\\\t<copyfile dest=\"${i}\" src=\"${i}\"/>" .repo/manifest.xml
        done
	sed -i '/path="frameworks\/base\/api"/a\\t<copyfile dest="frameworks/base/Android.mk" src="root.mk"/>' .repo/manifest.xml
	cd .repo/manifests
	git add .
	git commit -m "add copyfile for ${BASELINE_NAME}.xml"
	git push origin default:master
	repo forall -c git add -A || log_error "excute command faild, pls check your repository"
	repo forall -c git commit -m "Init ${BASELINE_NAME} source code" || log_error "excute command faild, pls check your repository"
	repo forall -c git push origin import || log_error "excute command faild, pls check your repository"
	rm -rf ./* || log_error "can not remove some files, pls check the access"
	repo sync -cj4
}

###main function###
deal_with_org_code
compare_pro_list
create_repos
upload_code
