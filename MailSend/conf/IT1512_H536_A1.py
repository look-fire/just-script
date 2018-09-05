Dict = {
    "PROJECT_NAME" : "H356",
    "PROJECT_JIRA_URL" : "http://192.168.1.75:8080/browse/ITYWYEHSWL",
    "PLATFORM":"MT6735",
    "XML_NAME":"it1512_gms",
    "VERSION_BASE":"it1512-H356A1",
    "SNAPSHOT_DIRECTORY":"h356_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6735/manifest -b master",
    "MODEM":"ssh://192.168.10.10/RLK6735_65C_L_LTTG_DSDS_CMCC_LWG_DSDS_CMCC_MOLY.LR9.W1444.MD.LWTG.CMCC.MP.01.V1.git ssh://192.168.10.10/RLK6735_65C_L_LTTG_DSDS_LWG_DSDS_MOLY.LR9.W1444.MD.LWTG.MP.01.V2.git",
    "BRANCH_NAME":"IT1512_GMS",
    "PROJECT_COMPLIE":"h356_a1",
    "BASE_PATH":"/mnt/SwVer4/北京合作项目/IT1512-H356/A1_BOM/GMS",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] KMQ820013M_B419","#define CS_PART_NUMBER[1] KMQ7X000SA_B315","#define CS_PART_NUMBER[2] KMF720012M_B214","#define CS_PART_NUMBER[3] 08EMCP08_EL3BT227"],
    "TO_MAIL_LIST":["yuanchun.yao@reallytek.com"],
    "CC_MAIL_LIST":["yuanchun.yao@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]
