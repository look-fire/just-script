#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "CXAir_H3713",
    "PLATFORM":"MT6737_N",
    "XML_NAME":"CXLite_H3713_HiOS2.0.0_N",
    "VERSION_BASE":"CXAir",
    "SNAPSHOT_DIRECTORY":"cxlite_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6737_N/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6737T_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"CXLite_H3713_HiOS2.0.0_N",
    "PROJECT_COMPLIE":"cxlite_h3713_a1",
    "BASE_PATH":"/mnt/SwVer4/TECNO/CXAir_H3713/A1_BOM/DAILY",
    "MEMORY":["#define BOARD_ID                MT6735_EVB","#define CS_PART_NUMBER[0]       H9TQ64A8GTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ7X000SA_B315","#define CS_PART_NUMBER[2]       H9TQ17ABJTMCUR_KUM"],
    "TO_MAIL_LIST":["yfybrjkfb@reallytek.com","yfybrjcsb@reallytek.com","shouhui.li@reallytek.com"],
    "CC_MAIL_LIST":["ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com","ptyfbgxb@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]

