#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X522-H539",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XWEEHWSJ",
    "PLATFORM":"MT6753",
    "XML_NAME":"X522_H539_MP1",
    "VERSION_BASE":"X522-H539A1",
    "SNAPSHOT_DIRECTORY":"x522_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6753/manifest -b master",
    "MODEM":"ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"X522_H539_MP1",
    "PROJECT_COMPLIE":"x522_h539_a1_id_3g",
    "BASE_PATH":"/mnt/SwVer4/X522_H539/X522_H539_MP1/a1_id_3g/DAILY",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[2] KMQE10013M_B318","#define CS_PART_NUMBER[3] H9TQ26ADFTACUR_KUM","#define CS_PART_NUMBER[4] KMRX1000BM_B614"],
    "TO_MAIL_LIST":["ruanjianyibu@reallytek.com","ptyfbgxb@reallytek.com","ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","weike.xu@reallytek.com","liang.zhang@reallytek.com"]
}
def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]
