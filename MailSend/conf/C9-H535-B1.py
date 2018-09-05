#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "C9",
    "PROJECT_JIRA_URL" : "http://192.168.1.75:8080/browse/CJHWSW",
    "PLATFORM":"MT6753",
    "XML_NAME":" C9_H535_HiOS_MP_GMS",
    "VERSION_BASE":"C9",
    "SNAPSHOT_DIRECTORY":"h535_release_tag",
    "BASE_URL":"repo init -u ssh://192.168.10.10:29418/MTK6753/manifest",
    "MODEM":"ssh://192.168.10.10/RLK6753_65C_L1_LTTG_DSDS_LWG_DSDS_MOLY.git",
    "BRANCH_NAME":"C9_H535_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"h535_b1",
    "BASE_PATH":"/mnt/SwVer4/C9-H535/B1_BOM/GMS/R8",
    "MEMORY":["#define BOARD_ID                MT6735_EVB","#define CS_PART_NUMBER[0]       KMQ820013M_B419","#define CS_PART_NUMBER[1]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[2]       H9TQ26ADFTACUR_KUM","#define CS_PART_NUMBER[3]       KMRX1000BM_B614","#define CS_PART_NUMBER[4]       KMQ4Z0013M_B809"],
    "TO_MAIL_LIST":["pengpeng.liang@reallytek.com","kun.mao@@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




