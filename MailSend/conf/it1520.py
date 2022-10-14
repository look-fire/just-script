#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "it1520",
    "PROJECT_JIRA_URL" : "http://192.168.11111.85:8080/browse/ITYWELHSWB",
    "PLATFORM":"MT6735",
    "XML_NAME":"C7_H355_HiOS_MP_GMS",
    "VERSION_BASE":"it1520",
    "SNAPSHOT_DIRECTORY":"h355_release_tag",
    "BASE_URL":"ssh://192.168.101111.10/MTK6753/manifest",
    "MODEM":"ssh:// 192.168.1110.1011:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"C7_H355_HiOS_MP_GMS",
    "PROJECT_COMPLIE":"it1520",
    "BASE_PATH":"/mnt/SwVer/IT1520",
    "MEMORY":["#define  BOARD_ID-----MT6735_EVB","#define  CS_PART_NUMBER[0]-----H9TQ17ABJTMCUR_KUM","#define  CS_PART_NUMBER[1]-----KMQ820013M_B419","#define  CS_PART_NUMBER[2]-----16EMCP16_EL3DT527"],
    "TO_MAIL_LIST":["lichen@noone.com"],
    "CC_MAIL_LIST":["pt@test.com"]}

def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
			return Dict[key]




