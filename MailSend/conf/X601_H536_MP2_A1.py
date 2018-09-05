Dict = {
    "PROJECT_NAME" : "X601-H536",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XLLYHWSL/",
    "PLATFORM":"MT6753",
    "XML_NAME":"X601_H536_XUI_MP2",
    "VERSION_BASE":"X601-H536A1",
    "SNAPSHOT_DIRECTORY":"x601_h536_a1_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6753/manifest -b master",
    "MODEM":"git clone ssh://192.168.10.10:29418/RLK6753_65T_M0_LTTG_DSDS_LTTG_DSDS_CDD48_LWG_DSDS_LWG_DSDS_CDD48_MOLY.LR9.W1444.MD.LWTG.MP.V79",
    "BRANCH_NAME":"X601_H536_XUI_MP2",
    "PROJECT_COMPLIE":"x601_h536_a1",
    "BASE_PATH":"/mnt/SwVer4/X601_H536/A1_BOM/MP/",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] KMQ820013M_B419","#define CS_PART_NUMBER[1] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[2] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[3] KMQE10013M_B318"],
    "TO_MAIL_LIST":["yuanchun.yao@reallytek.com"],
    "CC_MAIL_LIST":["yuanchun.yao@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]
