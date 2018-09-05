#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "E31_HiOS_N_CXAir",
    "PLATFORM":"MT6737_N",
    "XML_NAME":"E31_H375_HiOS2.0.0_N_DEV",
    "VERSION_BASE":"E31",
    "SNAPSHOT_DIRECTORY":"E31_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MT6737_N/manifest",
    "MODEM":"ssh://192.168.10.40:29418/RLK6737T_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"E31_H375_HiOS2.0.0_N_DEV",
    "PROJECT_COMPLIE":"e31_h375_a1",
    "BASE_PATH":"/mnt/SwVer4/TECNO/E31_HiOS_N_CXAir/A1_BOM/DAILY",
    "MEMORY":["#define CS_PART_NUMBER[0]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ820013M_B419",],
    "TO_MAIL_LIST":["ruanjianceshibu@reallytek.com","yfybrjkfb@reallytek.com"],
    "CC_MAIL_LIST":["shouhui.li@reallytek.com","bin.kou@reallytek.com","yongrong.wang@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]


