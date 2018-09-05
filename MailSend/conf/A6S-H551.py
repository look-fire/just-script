#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "A6S-H551",
    "PLATFORM":"MTK6755",
    "XML_NAME":"A6_H551_HiOS_MP",
    "VERSION_BASE":"A6S",
    "SNAPSHOT_DIRECTORY":"h551_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6755/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6755_65_M_LWCTG_MOLY.LR11.W1539.MD.MP.V9.git",
    "BRANCH_NAME":"A6_H551_HiOS_MP",
    "PROJECT_COMPLIE":"h551_c1",
    "BASE_PATH":"/mnt/SwVer4/A6_H551/HIOS/C1_BOM/R10",
    "MEMORY":["#define BOARD_ID                MT6755_EVB","#define CS_PART_NUMBER[0]       KMRE1000BM_B512","#define CS_PART_NUMBER[1]       H9TQ26ADFTACUR_KUM","#define CS_PART_NUMBER[2]       KMRX1000BM_B614","#define CS_PART_NUMBER[3]       H9TQ17ADFTACUR_KUM"],
    "TO_MAIL_LIST":["pengpeng.liang@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




