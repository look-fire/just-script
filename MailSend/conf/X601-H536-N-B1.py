Dict = {
    "PROJECT_NAME" : "X601-H536",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XLLYNHWSL/",
    "PLATFORM":"MT6753",
    "XML_NAME":"X601_H536_N_XOS",
    "VERSION_BASE":"X601-H536B1",
    "SNAPSHOT_DIRECTORY":"x601_h536_b1_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6753_N/manifest -b master",
    "MODEM":"git clone ssh://192.168.10.40:29418/RLK6753_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"X601_H536_N_XOS",
    "PROJECT_COMPLIE":"x601_h536_b1",
    "BASE_PATH":"/mnt/SwVer4/X601-H536-N/B1_BOM/DailyBuild",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] KMQ820013M_B419","#define CS_PART_NUMBER[1] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[2] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[3] KMQE10013M_B318"],
    "TO_MAIL_LIST":["haobin.zhang@reallytek.com","lijia.chen@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["yuanchun.yao@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","yongrong.wang@reallytek.com","zhen.wang@reallytek.com","dongming.lu@reallytek.com","weicheng.wang@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]
