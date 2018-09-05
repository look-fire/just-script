#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "WX4",
    "PLATFORM":"MT6580_N",
    "XML_NAME":"WX4_H8013_HiOS2.0.0_N",
    "VERSION_BASE":"WX4",
    # "BUILD_MODE":"user mtklog",
    "SNAPSHOT_DIRECTORY":"WX4_a1_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6580_N/manifest",
    "MODEM":"ssh://192.168.10.48:29418/RLK6580_WE_N_GPRS_HSPA_MOLY.WR8.W1449.MD.WG.MP.V91.5",
    "BRANCH_NAME":"WX4_H8013_HiOS2.0.0_N",
    "PROJECT_COMPLIE":"wx4_h8013_a1",
    "BASE_PATH":"/mnt/SwVer4/TECNO/WX4/A1_BOM/DAILY",
    "MEMORY":["#define BOARD_ID                MT6580_EVB","#define CS_PART_NUMBER[0]       KMFE10012M_B214"],
    "TO_MAIL_LIST":["ruanjianerbu@reallytek.com","ptyfbgxb@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianceshibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com"],
    "CC_MAIL_LIST":["hanfeng.wang@reallytek.com","lu.zheng@reallytek.com","zhen.wang@reallytek.com","yongrong.wang@reallytek.com","changkun.wu@reallytek.com","bingrong.xie@reallytek.com"]}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]


