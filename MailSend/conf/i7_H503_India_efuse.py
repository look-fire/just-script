#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "i7",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/PWYHWLS/",
    "PLATFORM":"MT6755_N",
    "XML_NAME":"i7_H503_India",
    "VERSION_BASE":"i7-H503A1",
    "SNAPSHOT_DIRECTORY":"i7_h503_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6755_N/manifest -b master",
    "MODEM":"ssh://192.168.10.40:29418/RLK6755_65_N_LWCTG_MP3_50_LWCTG_MP3_MOLY.LR11.W1603.MD.MP.V35.4",
    "BRANCH_NAME":"i7_H503_India",
    "PROJECT_COMPLIE":"i7_h503_a1_efuse",
    "BASE_PATH":"/mnt/SwVer4/i7/i7_H503_India/A1_BOM_EFUSE/DAILY",
    "MEMORY":["#define CS_PART_NUMBER[0] KMRX10014M_B614","#define CS_PART_NUMBER[1] H9TQ26ACLTMCUR_KUM"],
    "TO_MAIL_LIST":["xywrjcsb@reallytek.com","ptyfbgxb@reallytek.com","yingjianbuceshi@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com","xywxmglb@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","shaoping.gu@reallytek.com","liang.zhang@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]

