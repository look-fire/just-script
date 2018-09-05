#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "i5",
    "PLATFORM":"MT6737_N",
    "XML_NAME":"i5_H379_India",
    "VERSION_BASE":"i5",
    "SNAPSHOT_DIRECTORY":"D41_release_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6737_N/manifest",
    "MODEM":"git clone ssh:// 192.168.10.10:29418/RLK6753_65C_1_L1_LTTG_DSDS_LWG_DSDS_MOLY.LR9.W1444.MD.LWTG.MP.V36",
    "BRANCH_NAME":"i5_H379_India",
    "PROJECT_COMPLIE":"i5_h379_b1_efuse",
    "BASE_PATH":"/mnt/SwVerTemp/i5/i5_H379_india_pr1/d41_h379_a1/Release",
    "MEMORY":["#define CS_PART_NUMBER[3]       KMRX1000BM_B614",],
    "TO_MAIL_LIST":["xywrjcsb@reallytek.com","xywrjkfb@reallytek.com","xywxmglb@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ptyfbgxb@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","wei.liu2@reallytek.com","yong.yang2@reallytek.com","xiangsheng.xia@reallytek.com","yongrong.wang@reallytek.com","zhen.wang@reallytek.com","haobin.zhang@reallytek.com","shaoping.gu@reallytek.com","wei.zhao3@reallytek.com"]}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]


