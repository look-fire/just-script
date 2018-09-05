#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X556_H371",
    "PLATFORM":"MTK6737",
    "XML_NAME":"X556_H371_XUI_MP1",
    "VERSION_BASE":"X556-H371A1-M-ID-SKD",
    "SNAPSHOT_DIRECTORY":"X556_H371_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6737/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6737_65_M0_LTG_DSDS_LTG_DSDS_COTSX_LWG_DSDS_LWG_DSDS_COTSX_MOLY.LR9.W1444.MD.LWTG.MP.V81.6",
    "BRANCH_NAME":"X556_H371_XUI_MP1",
    "PROJECT_COMPLIE":"x556_h371_a1_id_4g",
    "BASE_PATH":"/mnt/SwVer4/X556_H371/xui/ID/TSM/RELEASE",
    "MEMORY":["#define CS_PART_NUMBER[0]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ820013M_B419"],
    "TO_MAIL_LIST":["haobin.zhang@reallytek.com","kang.li@reallytek.com","ruanjianceshibu@reallytek.com"],
    #"TO_MAIL_LIST":["haobin.zhang@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","wei.zhang@reallytek.com","junpu.tong@reallytek.com","zihao.ji@reallytek.com"]}
    #"CC_MAIL_LIST":["haobin.zhang@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




