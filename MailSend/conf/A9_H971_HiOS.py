#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "A9_H971_HiOS",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/AJHJQY",
    "PLATFORM":"MTK6797",
    "XML_NAME":"A9_H971_HiOS_MP",
    "VERSION_BASE":"A9-H971",
    "SNAPSHOT_DIRECTORY":"h971_a_hios_tag",
    "BASE_URL":"ssh://192.168.10.10:29418/MTK6797/manifest",
    "MODEM":"ssh://scm@192.168.10.10:29418/RLK6797_5T_M_LWCTG_MOLY.LR11.W1539.MD.MP.V15",
    "BRANCH_NAME":"A9_H971_HiOS_MP",
    "PROJECT_COMPLIE":"a9_h971_a1_hios",
    "BASE_PATH":"/mnt/SwVer4/A9_H971_HiOS/A1_BOM/HIOS",
    "MEMORY":["#define  BOARD_ID-----MT6797_EVB","#define  CS_PART_NUMBER[0]-----H9CKNNNDATMUPR" ,"#define  CS_PART_NUMBER[1]-----H9CKNNNCPTMRPR","#define  CS_PART_NUMBER[2]-----K3QF6F60AM ","#define  CS_PART_NUMBER[3]-----K3QF4F40BM ","#define  CS_PART_NUMBER[4]-----EDFP164A3PD ","#define  CS_PART_NUMBER[5]-----MT52L512M64D4GN"],
    "TO_MAIL_LIST":["dexiang.zhang@reallytek.com","shouhui.li@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianerbu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




