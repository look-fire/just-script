#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "L8-Plus埃及",
    "PROJECT_JIRA_URL" : "http://192.168.1.75:8080/browse/LBHBLW",
    "PLATFORM":"MT6580",
    "XML_NAME":"L8_H805_HiOS_MP_GMS",
    "VERSION_BASE":"L8PLUS",
    "SNAPSHOT_DIRECTORY":"h805_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6580/manifest",
    "MODEM":"ssh://192.168.10.10/MT6580_MODEM_WE_L_GPRS_HSPA_MP_V6.git",
    "BRANCH_NAME":"L8_H805_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"h805_b2_plus",
    "MAKE_MODE":"true",
    "BASE_PATH":u"/mnt/SwVer4/北京合作项目/L8-H805/BD_BOM/GMS/PLUS",
    "MEMORY":["#define BOARD_ID-----MT6580_EVB","#define CS_PART_NUMBER[0]-----KMQ820013M_B419","#define CS_PART_NUMBER[1]-----16EMCP16_EL3CV100","#define CS_PART_NUMBER[2]-----H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[3]-----KMQE10013M_B318","#define CS_PART_NUMBER[4]-----16EMCP16_NL3ET527"],
    "TO_MAIL_LIST":["lichen.yu@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","xiangfu.dang@transage.cn","ruijie.zhang@transage.cn","jinlei.mo@transage.cn","weifeng.niu@transage.cn","jianjun.han@transage.cn","yuebin.zhang@transage.cn","junfeng.shi@transage.cn","qing.yang@transage.cn","qing.yang@transage.cn","haitao.wang@transage.cn","daqi.zhang@transage.cn","yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




