#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X5511-H3716",
    "PROJECT_JIRA_URL" :"http://192.168.1.85:8080/browse/XWWYYHSQYL/",
    "PLATFORM":"MTK6737",
    "XML_NAME":"X5511_H3716_XUI_IN",
    "VERSION_BASE":"X5511-H3716A1-M-IN",
    "SNAPSHOT_DIRECTORY":"X556_H371_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6737/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6737_65_M0_LTG_DSDS_LTG_DSDS_COTSX_LWG_DSDS_LWG_DSDS_COTSX_MOLY.LR9.W1444.MD.LWTG.MP.V81.6",
    "BRANCH_NAME":"X5511_H3716_XUI_IN",
    "PROJECT_COMPLIE":"x5511_h3716_a1",
    "BASE_PATH":"/mnt/SwVer4/INFINIX/X5511_H3716/XUI/A1_BOM/DAILY",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1] KMQ820013M_B419","#define CS_PART_NUMBER[2] KMQE10013M_B318","#define CS_PART_NUMBER[3] KMRE1000BM_B512","#define CS_PART_NUMBER[4] KMFE10012M_B214"],
    "TO_MAIL_LIST":["ruanjianceshibu@reallytek.com","ptyfbgxb@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com"],
    "CC_MAIL_LIST":["yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com","kang.li@reallytek.com","liang.zhang@reallytek.com"]
}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]

