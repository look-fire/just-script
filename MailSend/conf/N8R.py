#!/usr/bin/python
# coding: utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "N8V-H356",
    "PLATFORM":"MT6735",
    "XML_NAME":"N8R_H356_itel",
    "VERSION_BASE":"N8V",
    "SNAPSHOT_DIRECTORY":"n8r_h356_release_tag",
    "BASE_URL":"ssh://192.168.10.40:29418/MTK6753/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"N8R_H356_itel",
    "PROJECT_COMPLIE":"n8r_e1_n8",
    "BASE_PATH":"/mnt/SwVerTemp/北京合作项目/N8R-H356/VODAFONE/E1_BOM",
    "MEMORY":["#define BOARD_ID      MT6735_EVB","#define CS_PART_NUMBER[0]       KMQ820013M_B419","#define  CS_PART_NUMBER[1]  KMQ7X000SA_B315","#define CS_PART_NUMBER[2]       KMF720012M_B214"],
    "TO_MAIL_LIST":["wei.liu2@reallytek.com","ruanjianerbu@reallytek.com","ptyfbgxb@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","ptyfbptrjb@reallytek.com"],
    "CC_MAIL_LIST":["changkun.wu@reallytek.com","sangui.zhang@reallytek.com","yongrong.wang@reallytek.com","zhen.wang@reallytek.com","haobin.zhang@reallytek.com"]
}
def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                   return Dict[key]


