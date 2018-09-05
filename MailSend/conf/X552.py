#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X552",
    "PLATFORM":"MTK6795",
    "XML_NAME":"X552_H952_XUI_MP1",
    "VERSION_BASE":"X552",
    "SNAPSHOT_DIRECTORY":"h952_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6795/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6795_LWT_M_LTTG_LWG_MOLY.LR9.W1444.MD.LWTG.MP.V67.4",
    "BRANCH_NAME":"X552_H952_XUI_MP1",
    "PROJECT_COMPLIE":"H952_A_Bom",
    "BASE_PATH":"/mnt/SwVerTemp/X552M-H952/A1_BOM/MP1",
    "MEMORY":["#define CS_PART_NUMBER[0]       KMF820012M_B305","#define CS_PART_NUMBER[1]       16EMCP08_EL3CV100","#define CS_PART_NUMBER[2]       KMQ8X000SA_B414","#define CS_PART_NUMBER[3]       KMQ82000SM_B418"],
    "TO_MAIL_LIST":["wei.liu2@reallytek.com","kang.li@reallytek.com","ruanjianyibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ruanjianceshibu@reallytek.com","yingjianbuceshi@reallytek.com","ptyfbptrjb@reallytek.com"],
    "CC_MAIL_LIST":["changkun.wu@reallytek.com"]
}
def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                   return Dict[key]
