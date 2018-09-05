#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "AX8_H571",
    "PLATFORM":"MT6757_N",
    "XML_NAME":"MT6757_N_DRV_ONLY",
    "VERSION_BASE":"AX7",
    "SNAPSHOT_DIRECTORY":"h571_india_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6757_N/manifest -b master",
    "MODEM":"ssh://192.168.10.48:29418/RLK6757_66_N_LWCTG_MP5_MOLY.LR11.W1630.MD.MP.V9.3",
    "BRANCH_NAME":"MT6757_N_DRV_ONLY",
    "PROJECT_COMPLIE":"h571",
    "BASE_PATH":"/mnt/SwVer4/TECNO/AX8_H571/DAILY",
    "MEMORY":["#define BOARD_ID MT6757_EVB","#define CS_PART_NUMBER[0] H9HP52ACPMMDAR","#define CS_PART_NUMBER[1] KMWX10016M_B619","#define CS_PART_NUMBER[2] KMWC10016M_B812","#define CS_PART_NUMBER[3] KMWC10017M_B812","#define CS_PART_NUMBER[4] H9TQ26ADFTBCUR","#define CS_PART_NUMBER[5] H9HP27ACVUMDAR"],
    "TO_MAIL_LIST":["yfybrjkfb@reallytek.com","yfybrjcsb@reallytek.com","qifeng.xie@reallytek.com"],
    "CC_MAIL_LIST":["ruanjianxiangmuguanlibu@reallytek.com","ptyfbptrjb@reallytek.com","ptyfbgxb@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
		   return Dict[key]




