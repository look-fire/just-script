#!/bin/bash
#Transsion Top Secret
##Create branch for some projects based to snapshot
##e.g. bash ${0} ssh://192.168.10.10/MTK6580/manifest h801_release_tag/L5-H805-A1-L-201601261651.xml project.list
readonly BASE_URL="$1"
readonly SNAP_XML="$2"
#readonly PRO_LIST="$3"

function down_code(){
	[ -d "CODEBASR" ] && rm -rf "CODEBASR"
	mkdir "CODEBASR" && cd "CODEBASR" || exit 1
	cp ../PRO_LIST .
	pathroot="$(pwd)"
	CMD="repo init -u ${BASE_URL} -m ${SNAP_XML}"
	$CMD
	#for i in $(cat "${PRO_LIST}")
	while read -r line 
	do
		repo sync "${line}" -cj4
	done <  PRO_LIST
}

function get_branch()
{
#	time=`echo ${SNAP_XML} | grep -oP '\d{12}'`
#	echo $time
#	branch=${time}_update
	xmlfile=$(basename "${SNAP_XML}")
	branch=${xmlfile%.*}
	branch=${branch//_update/}
	branch=${branch}_update
	repo start "${branch}" --all
	repo forall -c 'git push $REPO_REMOTE '${branch}''
}

function modify_snap_xml()
{
	cp "${pathroot}"/.repo/manifests/"${SNAP_XML}" "${pathroot}"/.repo/manifests/"${branch}".xml
	sed -i 's/\//\\\//g' PRO_LIST
	while read -r line
	do 
		cd "${pathroot}"/.repo/manifests || exit 1
		sed -i "/${line}/s/revision=\"[a-z0-9]\{40\}\"/revision=\"${branch}\"/" "${branch}".xml
	done < PRO_LIST
	xmllint "${branch}".xml
	if [ ${PIPESTATUS} -ne 0 ]
	then
		echo "error ${branch}.xml" && exit 1
	fi
	git add .
	git commit -m "time:$(date +%Y-%m-%d-%H-%M) base to ${SNAP_XML} add ${branch}.xml"
	git push origin HEAD:master
}

down_code
get_branch
modify_snap_xml
