#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "N1_Lite",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/NLIT",
    "PLATFORM":"MTK6580",
    "BUILD_MODE":"gmo_user",
    "XML_NAME":"N1Lite_H8016_M",
    "VERSION_BASE":"N1Lite",
    "SNAPSHOT_DIRECTORY":"n1lite_a1",
    "BASE_URL":"ssh://192.168.10.40/MTK6580/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6580_WE_M_GPRS_HSPA_MOLY.WR8.W1449.MD.WG.MP.V59",
    "BRANCH_NAME":"N1Lite_H8016_M",
    "PROJECT_COMPLIE":"n1lite_a1",
    "BASE_PATH":u"/mnt/SwVer4/N1_Lite/A1_BOM/DAILY",
    "MEMORY":["#define BOARD_ID                MT6580_EVB","#define CS_PART_NUMBER[0]       KMF720012M_B214" ,"#define CS_PART_NUMBER[1]      >08EMCP08_EL3BT227","#define CS_PART_NUMBER[2]       08EMCP04_EL3BT227"],
    "TO_MAIL_LIST":["mengmeng.zhang@reallytek.com","shouhui.li@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




