#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "i3",
    "PLATFORM":"MT6737_N",
    "XML_NAME":"E31_H375_India",
    "VERSION_BASE":"i3",
    "SNAPSHOT_DIRECTORY":"E31_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6737_N/manifest",
    "MODEM":"git clone ssh://192.168.10.40:29418/RLK6737T_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"E31_H375_India",
    "PROJECT_COMPLIE":"i3_h375_c1_65_efuse",
    "BASE_PATH":"/mnt/SwVerTemp/i3/E31_H375_India",
    "MEMORY":["#define CS_PART_NUMBER[0]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ820013M_B419",],
    "TO_MAIL_LIST":["xywrjcsb@reallytek.com","xywrjkfb@reallytek.com","xywxmglb@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ptyfbgxb@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","shaoping.gu@reallytek.com","wei.liu2@reallytek.com","yongrong.wang@reallytek.com","zhen.wang@reallytek.com","haobin.zhang@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]

