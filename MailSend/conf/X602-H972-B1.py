#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X602-H972",
    "PLATFORM":"MT6797",
    "XML_NAME":"X602_H972_XUI",
    "VERSION_BASE":"X602-H972",
    "SNAPSHOT_DIRECTORY":"h972_b1_tag",
    "BASE_URL":"repo init -u ssh://192.168.10.10:29418/MTK6797/manifest",
    "MODEM":"ssh://192.168.10.10:29418/RLK6797_5T_M_LWCTG_MOLY.LR11.W1539.MD.MP.V15.git",
    "BRANCH_NAME":"X602_H972_XUI",
    "PROJECT_JIRA_URL":"http://192.168.1.85:8080/browse/XLLEHJQE/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel",
    "PROJECT_COMPLIE":"x602_h972_b1",
    "BASE_PATH":"/mnt/SwVer/X602_H972/B1_BOM",
    "MEMORY":["#define BOARD_ID MT6797_EVB","#define CS_PART_NUMBER[0] H9CKNNNDATMUPR","#define CS_PART_NUMBER[1] H9CKNNNCPTMRPR","#define CS_PART_NUMBER[2] K3QF6F60AM","#define CS_PART_NUMBER[3] K3QF4F40BM","#define CS_PART_NUMBER[4] EDFP164A3PD","#define CS_PART_NUMBER[5] MT52L512M64D4GN"],
    "TO_MAIL_LIST":["weicheng.wang@reallytek.com"],
    "CC_MAIL_LIST":["weicheng.wang@reallytek.com"]
}
def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
		   return Dict[key]




