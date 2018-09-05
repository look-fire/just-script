#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "H355",
    "PROJECT_JIRA_URL" : "http://192.168.1.75:8080/browse/CQHSWW",
    "PLATFORM":"MTK6753",
    "XML_NAME":"C7_H355_HiOS_MP_GMS",
    "VERSION_BASE":"C7",
    "SNAPSHOT_DIRECTORY":"h355_release_tag",
    "BASE_URL":"repo init -u ssh://192.168.10.10/MTK6753/manifest",
    "MODEM":"git clone ssh:// 192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"C7_H355_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"c7_f1",
    "BASE_PATH":"/mnt/SwVer4/C7_H355/F1_BOM/GMS",
    "MEMORY":["#define BOARD_ID    MT6735_EVB","#define CS_PART_NUMBER[0]   H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1]   KMQ820013M_B419","#define CS_PART_NUMBER[2]    16EMCP16_EL3DT527","#define CS_PART_NUMBER[3]      KMQE10013M_B318"],
    "TO_MAIL_LIST":["lichen.yu@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




