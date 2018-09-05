#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "W3_H806",
    "PROJECT_JIRA_URL" : "http://192.168.1.75:8080/browse/WSHBLL",
    "PLATFORM":"MT6580",
    "XML_NAME":"W3_H806_HiOS_MP_GMS",
    "VERSION_BASE":"W3",
    "SNAPSHOT_DIRECTORY":"h806_release_tag",
    "BASE_URL":"ssh://192.168.10.40:29418/MTK6580/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6580_WE_M_GPRS_HSPA_MOLY.WR8.W1449.MD.WG.MP.V41",
    "BRANCH_NAME":"W3_H806_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"w3_a1",
    "BASE_PATH":u"/mnt/SwVer4/北京合作项目/W3-H806/NEW_BASE/A1_BOM/MP/GMS",
    "MEMORY":["#define BOARD_ID-----MT6580_EVB","#define CS_PART_NUMBER[0]-----KMF720012M_B214","#define CS_PART_NUMBER[1]-----H9TP64A8JDMCPR_KGM","#define CS_PART_NUMBER[2]-----KHN6405FS-HKc1","#define CS_PART_NUMBER[3]-----08EMCP08_EL3BT227","#define CS_PART_NUMBER[4]-----KMFNX0012M-B214","#define CS_PART_NUMBER[5]-----08EMCP08-NL3DT227"],
    "TO_MAIL_LIST":["lu.zheng@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","xiangfu.dang@transage.cn","ruijie.zhang@transage.cn","jinlei.mo@transage.cn","weifeng.niu@transage.cn","jianjun.han@transage.cn","yuebin.zhang@transage.cn","junfeng.shi@transage.cn","qing.yang@transage.cn","qing.yang@transage.cn","haitao.wang@transage.cn","daqi.zhang@transage.cn","yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




