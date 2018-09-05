Dict = {
    "PROJECT_NAME" : "X557-H807",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XWWQHBLQ/",
    "PLATFORM":"MT6580",
    "XML_NAME":"X557_XUI_MP1",
    "VERSION_BASE":"X557-H807C1",
    "SNAPSHOT_DIRECTORY":"x557_h807_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6580_M/manifest -b master",
    "MODEM":"git clone ssh://192.168.10.10/ RLK6580_WE_M_GPRS_HSPA_MOLY.WR8.W1449.MD.git",
    "BRANCH_NAME":"X557_XUI_MP1",
    "PROJECT_COMPLIE":"x557_h807_c1",
    "BASE_PATH":"/mnt/SwVer4/X557_H807/C1_BOM/MP",
    "MEMORY":["#define BOARD_ID MT6580_EVB","#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1] KMQ820013M_B419","#define CS_PART_NUMBER[2] KMF820012M_B305","#define CS_PART_NUMBER[3] 16EMCP08_EL3BT527"],
    "TO_MAIL_LIST":["yuanchun.yao@reallytek.com"],
    "CC_MAIL_LIST":["yuanchun.yao@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]
