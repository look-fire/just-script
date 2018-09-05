#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X555",
    "PLATFORM":"MTK6753",
    "XML_NAME":"X555_H538_XUI_MP1",
    "VERSION_BASE":"X555-H538A1-M",
    "SNAPSHOT_DIRECTORY":"x555_h538_release_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6753/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6737_65_M0_LTG_DSDS_LTG_DSDS_COTSX_LWG_DSDS_LWG_DSDS_COTSX_MOLY.LR9.W1444.MD.LWTG.MP.V81.6",
    "BRANCH_NAME":"X555_H538_XUI_MP1",
    "PROJECT_COMPLIE":"x555_h538_a1",
    "BASE_PATH":"/mnt/SwVer4/X555_H538/A1_BOM/MP1",
    "MEMORY":["#define CS_PART_NUMBER[0]       KMRX1000BM_B614","#define CS_PART_NUMBER[1]       H9TQ26ADFTACUR_KUM"],
    "TO_MAIL_LIST":["wei.liu2@reallytek.com","longlong.li@reallytek.com","ruanjianyibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","ptyfbptrjb@reallytek.com","ptyfbgxb@reallytek.com"],
    "CC_MAIL_LIST":["changkun.wu@reallytek.com","jinxia.cheng@reallytek.com","wei.zhang@reallytek.com","chengdong.wu@reallytek.com","yongrong.wang@reallytek.com","haobin.zhang@reallytek.com","zhen.wang@reallytek.com"]
}
def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                   return Dict[key]


