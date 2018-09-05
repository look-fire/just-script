#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "XOS_N",
    "PROJECT_JIRA_URL":"http://192.168.1.85:8080/browse/XOSN",
    "PLATFORM":"MTK6753",
    "XML_NAME":"XOS2.2.0_N_MP",
    "VERSION_BASE":"XOS",
    "SNAPSHOT_DIRECTORY":"xos_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6753_N/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"XOS2.2.0_N_MP",
    "PROJECT_COMPLIE":"x601_h536_a1",
    "BASE_PATH":"/mnt/SwVer4/XOS-N/DAILY/A1_BOM/XOS2.2.0_N_MP",
    "MEMORY":["#define BOARD_ID                MT6735_EVB","#define CS_PART_NUMBER[0]       KMQ820013M_B419","#define CS_PART_NUMBER[1]               16EMCP16_EL3DT527","#define CS_PART_NUMBER[2]       H9TQ17ABJTMCUR_KUM"],
    "TO_MAIL_LIST":["haobin.zhang@reallytek.com","chenlin.shu@reallytek.com","ruanjianceshibu@reallytek.com","weikang.wang@reallytek.com"],
    #"TO_MAIL_LIST":["haobin.zhang@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}
    #"CC_MAIL_LIST":["haobin.zhang@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




