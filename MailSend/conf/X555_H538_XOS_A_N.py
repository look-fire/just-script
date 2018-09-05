#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X555-H538-N",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XWWWHWSBN",
    "PLATFORM":"MT6753_N",
    "XML_NAME":"X555_H538_N_XOS",
    "VERSION_BASE":"X555-H538A1",
    "SNAPSHOT_DIRECTORY":"X555_XOSN_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6753_N/manifest -b master",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"X555_H538_N_XOS",
    "PROJECT_COMPLIE":"x555_h538_a1",
    "BASE_PATH":"/mnt/SwVer4/X555_H538_N/X555_H538_N_XOS/A1_BOM/DAILY",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] KMQ820013M_B419","#define CS_PART_NUMBER[1] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[2] H9TQ17ABJTMCUR_KUM","//#define CS_PART_NUMBER[3] H9TQ26ABJTMCUR_KUM","//#define CS_PART_NUMBER[4] KMR820001M_B609","#define CS_PART_NUMBER[3] KMRX1000BM_B614","#define CS_PART_NUMBER[4] H9TQ26ADFTACUR_KUM"],
    "TO_MAIL_LIST":["ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ptyfbgxb@reallytek.com","ptyfbsxb@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","sangui.zhang@reallytek.com","longlong.li@reallytek.com","liang.zhang@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]

