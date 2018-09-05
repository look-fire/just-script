#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "X521",
    "PLATFORM":"MTK6753_M_X520",
    "XML_NAME":"X521-J5088-XUI-MP1-R5",
    "VERSION_BASE":"X521-J5088A1",
    "SNAPSHOT_DIRECTORY":"x521_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6753_M_X520/manifest",
    "MODEM":"ssh://10.30.30.10/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.git",
    "PROJECT_JIRA_URL":"http://192.168.1.75:8080/browse/XWELGJWLBL",
    "BRANCH_NAME":"X521-J5088-XUI-MP1-R5",
    "PROJECT_COMPLIE":"x521_a1_id_4g",
    "BASE_PATH":"/mnt/SwVer/X521/PR2NewGerBer/A1_BOM/MP-R5",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[1] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[2] H9TQ26ADFTMCUR_KUM","//#define CS_PART_NUMBER[2] H9TQ17ADFTACUR_KUM","//#define CS_PART_NUMBER[3] KMR820001M_B609","//#define CS_PART_NUMBER[0] H9TP64A8JDMCPR_KGM","//#define CS_PART_NUMBER[4] KMF820012M_B305","#define CS_PART_NUMBER[2] KMQ820013M_B419","//#define CS_PART_NUMBER[6] KMR31000BA_B614","//#define CS_PART_NUMBER[4] KMRE1000BM_B512"],
    "TO_MAIL_LIST":["weicheng.wang@reallytek.com"],
    "CC_MAIL_LIST":["weicheng.wang@reallytek.com"]
}
def getInfo(pj_info):
	pj_info=pj_info
	for key in Dict.keys():
		if key==pj_info:
		   return Dict[key]




