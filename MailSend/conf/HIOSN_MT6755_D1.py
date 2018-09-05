#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "HIOSN_MT6755",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/HIOSGNGREL/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel",
    "PLATFORM":"MT6755",
    "XML_NAME":"HIOS2.0.0_N_DEV_MT6755",
    "VERSION_BASE":"HIOS-N",
    "SNAPSHOT_DIRECTORY":"HIOSN_MT6755_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6755_N/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6755_65_N_LWCTG_MP3_50_LWCTG_MP3_MOLY.LR11.W1603.MD.MP.V35.4",
    "BRANCH_NAME":"HIOS2.0.0_N_DEV_MT6755",
    "PROJECT_COMPLIE":"cx_h501_d1",
    "BASE_PATH":u"/mnt/SwVer4/CX_H501_N/CX_H501_HiOS/DAILY/D1_BOM/",
    "MEMORY":["#define BOARD_ID-----MT6755_EVB","#define CS_PART_NUMBER[0] KMRX1000BM_B614","#define CS_PART_NUMBER[1] KMRE1000BM_B512","#define CS_PART_NUMBER[2] H9TQ17ADFTACUR_KUM","#define CS_PART_NUMBER[3] KMQE10013M_B318"],
    "TO_MAIL_LIST":["weicheng.wang@reallytek.com","ruanjianceshibu@reallytek.com","ruanjianerbu@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","zhen.wang@reallytek.com","bin.kou@reallytek.com","changkun.wu@reallytek.com"]
}

def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]




