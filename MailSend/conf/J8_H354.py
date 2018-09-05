#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "J8_H354",
    "PROJECT_JIRA_URL" : "http://192.168.1.75:8080/browse/JBHSLS",
    "PLATFORM":"MT6735",
    "XML_NAME":"j8l_master_hios_mp_gms",
    "VERSION_BASE":"J8",
    "SNAPSHOT_DIRECTORY":"h354_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6753/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65C_1_L1_LTTG_DSDS_LWG_DSDS_MOLY.LR9.W1444.MD.LWTG.MP.V36",
    "BRANCH_NAME":"j8l_master_hios_mp_gms",
    "PROJECT_COMPLIE":"h354_j8l_hios_13m",
    "BASE_PATH":u"/mnt/SwVer4/J8-H354/合入HIOS版本/PR3/MP/GMS",
    "MEMORY":["#define BOARD_ID                MT6735_EVB","#define CS_PART_NUMBER[0]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ820013M_B419","#define CS_PART_NUMBER[2]>------KMQ4Z0013M_B809","#define CS_PART_NUMBER[3]>------H9TQ17ABJTACUR_KUM","#define CS_PART_NUMBER[4]>------KMQE10013M_B318"],
    "TO_MAIL_LIST":["kun.mao@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ptyfbgxb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}
def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]



