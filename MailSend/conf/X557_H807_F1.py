Dict = {
    "PROJECT_NAME" : "X557-H807",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XWWQHBLQ/",
    "PLATFORM":"MT6580",
    "XML_NAME":"X557_XUI_MP1",
    "VERSION_BASE":"X557-H807F1G1",
    "SNAPSHOT_DIRECTORY":"x557_h807_release_tag",
    "BASE_URL":"ssh://192.168.10.10/MTK6580_M/manifest -b master",
    "MODEM":"git clone ssh://192.168.10.10/ RLK6580_WE_M_GPRS_HSPA_MOLY.WR8.W1449.MD.git",
    "BRANCH_NAME":"X557_XUI_MP1",
    "PROJECT_COMPLIE":"x557_h807_f1",
    "BASE_PATH":"/mnt/SwVer4/X557_H807/F1_BOM/MP",
    "MEMORY":["#define BOARD_ID MT6580_EVB","#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1] KMQ820013M_B419","#define CS_PART_NUMBER[2] 16EMCP16_NL3ET527","#define CS_PART_NUMBER[3] KMQE10013M_B318"],
    "TO_MAIL_LIST":["yuanchun.yao@reallytek.com","ruanjianceshibu@reallytek.com","haobin.zhang@reallytek.com"],
    "CC_MAIL_LIST":["ptyfbptrjb@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","ruanjianyibu@reallytek.com","ptyfbgxb@reallytek.com","changkun.wu@reallytek.com","yongrong.wang@reallytek.com","zhen.wang@reallytek.com","dongming.lu@reallytek.com","weicheng.wang@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]
