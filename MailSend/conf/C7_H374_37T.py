#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "H374",
    "PLATFORM":"MTK6737",
    "XML_NAME":"C7_H374_HiOS_37T",
    "VERSION_BASE":"C7",
    "SNAPSHOT_DIRECTORY":"h374_release_tag",
    "BASE_URL":"repo init -u ssh://192.168.10.10:29418/MTK6737/manifest",
    "MODEM":"git clone ssh://192.168.10.10:29418/RLK6737T_65_M0_LTG_DSDS_LTG_DSDS_COTSX_LWG_DSDS_LWG_DSDS_COTSX_MOLY.LR9.W1444.MD.LWTG.MP.V81.6",
    "BRANCH_NAME":"C7_H374_HiOS_37T",
    "PROJECT_COMPLIE":"c7",
    "BASE_PATH":"/mnt/SwVer/C7_H374_37T",
    "MEMORY":["#define BOARD_ID                MT6735_EVB","#define CS_PART_NUMBER[0]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ820013M_B419","#define CS_PART_NUMBER[2]       KMQ4Z0013M_B809"],
    "TO_MAIL_LIST":["jie.xu@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




