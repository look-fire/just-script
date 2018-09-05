#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X601-H537",
    "PLATFORM":"MTK6753",
    "XML_NAME":"X601-H537A1-M-ID-201610210800",
    "VERSION_BASE":"X601-H537A1-M-ID-SKD",
    "SNAPSHOT_DIRECTORY":"x601_h537_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6753/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"X601_H536_XUI_MP1",
    "PROJECT_COMPLIE":"x601_h537_a1_in_4g",
    "BASE_PATH":"/mnt/SwVer/X601-H537/A1_BOM/YN",
    "MEMORY":["#define BOARD_ID                MT6735_EVB","#define CS_PART_NUMBER[0]       KMQ820013M_B419","#define CS_PART_NUMBER[1]       16EMCP16_EL3DT527",
	      "#define CS_PART_NUMBER[2]       H9TQ17ABJTMCUR_KUM"],
    "TO_MAIL_LIST":["haobin.zhang@reallytek.com","lijia.chen@reallytek.com","ruanjianceshibu@reallytek.com"],
    #"TO_MAIL_LIST":["haobin.zhang@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}
    #"CC_MAIL_LIST":["haobin.zhang@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




