#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "N8S-H356",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/NBSHSWL/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel",
    "PLATFORM":"MT6580",
    "XML_NAME":"N8S_H356_HiOS_MP_GMS",
    "VERSION_BASE":"N8S",
    "SNAPSHOT_DIRECTORY":"n8s_h356_release_tag",
    "BASE_URL":"ssh://192.168.10.40:29418/MTK6753/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"N8S_H356_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"n8s_b1",
    "BASE_PATH":u"/mnt/SwVer4/北京合作项目/N8S-H356/B1_BOM/GMS",
    "MEMORY":["#define BOARD_ID-----MT6735_EVB","#define CS_PART_NUMBER[0]-----KMQ820013M_B419","#define CS_PART_NUMBER[1]-----KMQ7X000SA_B315","#define CS_PART_NUMBER[2]-----KMF720012M_B214","#define CS_PART_NUMBER[3]-----08EMCP08_EL3BT227"],
    "TO_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","dongming.lu@reallytek.com","shuqi.yu@reallytek.com"],
    "CC_MAIL_LIST":["xiangfu.dang@transage.cn","ruijie.zhang@transage.cn","jinlei.mo@transage.cn","weifeng.niu@transage.cn","jianjun.han@transage.cn","yuebin.zhang@transage.cn","junfeng.shi@transage.cn","qing.yang@transage.cn","haitao.wang@transage.cn","daqi.zhang@transage.cn","yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com"]}

def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]




