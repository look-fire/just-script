#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X556-H371-N",
    "PROJECT_JIRA_URL" :"http://192.168.1.85:8080/browse/XWWLHSQYN/",
    "PLATFORM":"MTK6737_N",
    "XML_NAME":"X556_N_INDIA",
    "VERSION_BASE":"X556-H371A1-N",
    "SNAPSHOT_DIRECTORY":"X556_H371N_release_tag",
    "BASE_URL":"ssh://192.168.10.48/MT6737_N/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6737T_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"X556_N_INDIA",
    "PROJECT_COMPLIE":"x556_h371_a1_35_g",
    "BASE_PATH":"/mnt/SwVer4/INFINIX/X556_H371_N/INDIA/a1_35_g/DAILY",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1] KMRE1000BM_B512","#define CS_PART_NUMBER[2] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[3] KMQE10013M_B318","#define CS_PART_NUMBER[4] KMFE10012M_B214"],
    "TO_MAIL_LIST":["ruanjianceshibu@reallytek.com","ptyfbgxb@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","zhanyang.duan@reallytek.com","liang.zhang@reallytek.com"]
}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]
