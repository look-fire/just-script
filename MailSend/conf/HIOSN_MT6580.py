#!/usr/bin/python
# coding: utf-8
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
Dict = {
    "PROJECT_NAME" : "HIOSN-DEV-MT6580",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/HIOSNDEV/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel",
    "PLATFORM":"MT6580",
    "XML_NAME":"HIOS2.0.0_N_L9Plus",
    "VERSION_BASE":"HIOS-N",
    "SNAPSHOT_DIRECTORY":"HIOSN_MT6580_release_tag",
    "BASE_URL":"ssh://192.168.10.40:29418/MT6580_N/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6755_65_N_LWCTG_MP3_50_LWCTG_MP3_MOLY.LR11.W1603.MD.MP.V35.4",
    "BRANCH_NAME":"HIOS2.0.0_N_L9Plus",
    "PROJECT_COMPLIE":"l9_h8011_a1",
    "BASE_PATH":u"/mnt/SwVer4/CX_H501_N/CX_H501_HiOS/DAILY/D1_BOM/",
    "MEMORY":["#define BOARD_ID-----MT6580_EVB","#define CS_PART_NUMBER[0] 16EMCP16_NL3ET527","#define CS_PART_NUMBER[1] KMQE10013M_B318"],
    "TO_MAIL_LIST":["weicheng.wang@reallytek.com","ruanjianceshibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com","yfybrjkfb@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","zhen.wang@reallytek.com","bin.kou@reallytek.com","changkun.wu@reallytek.com","haobin.zhang@reallytek.com"]
}

def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]




