#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "CXS-H501",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/CXHWLY/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel",
    "PLATFORM":"MTK6750T",
    "XML_NAME":"CX_H501_HiOS2.0.0_N",
    "VERSION_BASE":"CXS",
    "SNAPSHOT_DIRECTORY":"cx_h501_hios_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6755_N/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6755_65_N_LWCTG_MP3_50_LWCTG_MP3_MOLY.LR11.W1603.MD.MP.V35.4",
    "BRANCH_NAME":"CX_H501_HiOS2.0.0_N",
    "PROJECT_COMPLIE":"cxs_h501_d1",
    "BASE_PATH":u"/mnt/SwVer4/CX_H501_N/CX_H501_HiOS/DAILY/D1_CXS_BOM/",
    "MEMORY":["#define BOARD_ID-----MT6755_EVB","#define CS_PART_NUMBER[0] KMRX1000BM_B614","#define CS_PART_NUMBER[1] KMRE1000BM_B512","#define CS_PART_NUMBER[2] H9TQ17ADFTACUR_KUM","#define CS_PART_NUMBER[3] KMQE10013M_B318"],
    "TO_MAIL_LIST":["shenjiang.he@reallytek.com","ruanjianceshibu@reallytek.com","yuanchun.yao@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","yongrong.wang@reallytek.com","zhen.wang@reallytek.com","dongming.lu@reallytek.com","weicheng.wang@reallytek.com"]
}

def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]




