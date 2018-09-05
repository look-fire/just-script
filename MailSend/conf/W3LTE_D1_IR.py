#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "W3LTE-H356",
    "PLATFORM":"MTK6753",
    "XML_NAME":"N8S_H356_HiOS_MP_GMS",
    "VERSION_BASE":"W3LTE",
    "SNAPSHOT_DIRECTORY":"n8_h356_release_tag",
    "BASE_URL":"ssh://192.168.10.40:29418/MTK6753/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"N8S_H356_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"w3lte_d1_ir",
    "BASE_PATH":u"/mnt/SwVer4/北京合作项目/W3LTE-H356/D1_BOM/GMS/IR",
    "MEMORY":["#define BOARD_ID-----MT6735_EVB","#define CS_PART_NUMBER[0]-----KMQ820013M_B419","#define CS_PART_NUMBER[1]-----KMQ7X000SA_B315","#define CS_PART_NUMBER[2]-----KMF720012M_B214","#define CS_PART_NUMBER[3]-----08EMCP08_EL3BT227","//#define CS_PART_NUMBER[0]-----H9TP64A8JDMCPR_KGM","//#define CS_PART_NUMBER[4]-----H9TP32A4GDDCPR_KGM"],
    "TO_MAIL_LIST":["shenjiang.he@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","xiangfu.dang@transage.cn","ruijie.zhang@transage.cn","jinlei.mo@transage.cn","weifeng.niu@transage.cn","jianjun.han@transage.cn","yuebin.zhang@transage.cn","junfeng.shi@transage.cn","qing.yang@transage.cn","qing.yang@transage.cn","haitao.wang@transage.cn","daqi.zhang@transage.cn"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




