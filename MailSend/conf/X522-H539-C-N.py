#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X522-H539-N",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XWEEHWSJN/",
    "PLATFORM":"MT6753_N",
    "XML_NAME":"X522_H539_N_XOS",
    "VERSION_BASE":"X522-H539C1",
    "SNAPSHOT_DIRECTORY":"X522_XOSN_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6753_N/manifest -b master",
    "MODEM":"ssh://192.168.10.40:29418/RLK6753_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"X522_H539_N_XOS",
    "PROJECT_COMPLIE":"x522_h539_c1",
    "BASE_PATH":"/mnt/SwVer4/INFINIX/X522_H539_N/X522_H539_N_XOS/C1_BOM/DAILY",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[2] KMQE10013M_B318","#define CS_PART_NUMBER[3] H9TQ26ADFTACUR_KUM","#define CS_PART_NUMBER[4] KMRX1000BM_B614"],
    "TO_MAIL_LIST":["ruanjianyibu@reallytek.com","ptyfbgxb@reallytek.com","ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","weike.xu@reallytek.com","liang.zhang@reallytek.com"]
}
def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]

