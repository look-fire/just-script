Dict = {
    "PROJECT_NAME" : "X601-H537",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XLLYHWSQ/",
    "PLATFORM":"MT6753",
    "XML_NAME":"X601_H536_XUI_MP1",
    "VERSION_BASE":"X601-H537C1",
    "SNAPSHOT_DIRECTORY":"x601_h537_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6753/manifest -b master",
    "MODEM":"git clone ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"X601_H536_XUI_MP1",
    "PROJECT_COMPLIE":"x601_h537_c1",
    "BASE_PATH":"/mnt/SwVer4/X601_H537/C1_BOM/MP/",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] KMRE1000BM_B512","#define CS_PART_NUMBER[1] H9TQ17ADFTACUR_KUM","#define CS_PART_NUMBER[2] KMQE10013M_B318","#define CS_PART_NUMBER[3] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[4] H9TQ17ABJTBCUR_KUM"],
    "TO_MAIL_LIST":["yuanchun.yao@reallytek.com"],
    "CC_MAIL_LIST":["yuanchun.yao@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]
