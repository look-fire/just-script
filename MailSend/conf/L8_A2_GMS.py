#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "L8",
    "PROJECT_JIRA_URL" : "http://192.168.1.75:8080/browse/LBHBLW",
    "PLATFORM":"MT6580",
    "XML_NAME":"L8_H805_HiOS_MP_GMS",
    "VERSION_BASE":"L8",
    "SNAPSHOT_DIRECTORY":"h805_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6580/manifest",
    "MODEM":"ssh://192.168.10.10/MT6580_MODEM_WE_L_GPRS_HSPA_MP_V6.git",
    "BRANCH_NAME":"L8_H805_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"h805_a2",
    "MAKE_MODE":"true",
    "BASE_PATH":u"/mnt/SwVer4/北京合作项目/L8-H805/A2_BOM/GMS",
    "MEMORY":["#define BOARD_ID-----MT6580_EVB","#define CS_PART_NUMBER[0]-----KMF820012M_B305","#define CS_PART_NUMBER[1]-----16EMCP08_EL3BT527","#define CS_PART_NUMBER[2]-----KMFE10012M_B214"],
    "TO_MAIL_LIST":["lichen.yu@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","xiangfu.dang@transage.cn","ruijie.zhang@transage.cn","jinlei.mo@transage.cn","weifeng.niu@transage.cn","jianjun.han@transage.cn","yuebin.zhang@transage.cn","junfeng.shi@transage.cn","qing.yang@transage.cn","qing.yang@transage.cn","haitao.wang@transage.cn","daqi.zhang@transage.cn","yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




