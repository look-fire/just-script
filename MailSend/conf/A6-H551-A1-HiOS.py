#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "A6_HiOS_N",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/HIOSN",
    "PLATFORM":"MT6755",
    "XML_NAME":"A6_HiOS_N",
    "VERSION_BASE":"A6-H551A1",
    "SNAPSHOT_DIRECTORY":"h551_HiOS_tag",
    "BASE_URL":"ssh://192.168.10.40:29418/MT6755_N/manifest -b master",
    "MODEM":"ssh://192.168.10.40:29418/RLK6755_65_N_LWCTG_MP3_50_LWCTG_MP3_MOLY.LR11.W1603.MD.MP.V35.4.git",
    "BRANCH_NAME":"A6_HiOS_N",
    "PROJECT_COMPLIE":"h551_a1",
    "BASE_PATH":"/mnt/SwVerTemp/A6_HiOS_N/DAILY",
    "MEMORY":["#define BOARD_ID MT6755_EVB","//#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR","//#define CS_PART_NUMBER[1] H9TQ17ABJTACUR","//#define CS_PART_NUMBER[2] H9TQ64AAETMCUR","//#define CS_PART_NUMBER[3] H9TQ26ADFTMCUR","#define CS_PART_NUMBER[0] KMRE1000BM_B512","#define CS_PART_NUMBER[1] H9TQ26ADFTACUR_KUM","#define CS_PART_NUMBER[2] KMRX1000BM_B614","#define CS_PART_NUMBER[3] H9TQ17ADFTACUR_KUM"],
    "TO_MAIL_LIST":["xywrjkfb@reallytek.com","ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com"],
    "CC_MAIL_LIST":["bin.kou@reallytek.com","yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","weicheng.wang@reallytek.com","yuanchun.yao@reallytek.com","dongming.lu@reallytek.com","wei.liu2@reallytek.com","shuqi.yu@reallytek.com","bingrong.xie@reallytek.com","liang.zhang@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]


