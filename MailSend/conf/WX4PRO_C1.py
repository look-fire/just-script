#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "WX4 Pro",
    "PLATFORM":"MT6737_N",
    "XML_NAME":"WX4Pro_H3712_HiOS2.0.0_N",
    "VERSION_BASE":"WX4Pro",
    #"BUILD_MODE":"user mtklog",
    "SNAPSHOT_DIRECTORY":"wx4_c1_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6737_N/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6737T_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"WX4Pro_H3712_HiOS2.0.0_N",
    "PROJECT_COMPLIE":"wx4_h3712_c1",
    "BASE_PATH":"/mnt/SwVer4/TECNO/WX4PRO/C1_BOM/DAILY",
    "MEMORY":["#define BOARD_ID    MT6735_EVB","#define CS_PART_NUMBER[0]       H9TQ64A8GTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ7X000SA_B315","#define CS_PART_NUMBER[2]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[3]       KMQE10013M_B318","#define CS_PART_NUMBER[4]       H9TQ17ABJTBCUR_KUM"],
    "TO_MAIL_LIST":["ruanjianerbu@reallytek.com","ptyfbgxb@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianceshibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com"],
    "CC_MAIL_LIST":["renzhi.li@reallytek.com","lichen.yu@reallytek.com","zhen.wang@reallytek.com","yongrong.wang@reallytek.com","changkun.wu@reallytek.com","bingrong.xie@reallytek.com"]}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]


