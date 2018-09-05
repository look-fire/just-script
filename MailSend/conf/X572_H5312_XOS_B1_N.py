Dict = {
    "PROJECT_NAME" : "X572-H5312",
    "PROJECT_JIRA_URL" : "http://192.168.1.85:8080/browse/XWQEHWSYE/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel",
    "PLATFORM":"MT6753N",
    "XML_NAME":"X572_H5312_XOS_V2.2.0_N",
    "VERSION_BASE":"X572-H5312B1",
    "SNAPSHOT_DIRECTORY":"x572_h5312_tag",
    "BASE_URL":"ssh://192.168.10.48:29418/MT6753_N/manifest -b master",
    "MODEM":"git clone ssh://192.168.10.40:29418/RLK6753_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"X572_H5312_XOS_V2.2.0_N",
    "PROJECT_COMPLIE":"x572_h5312_b1",
    "BASE_PATH":"/mnt/SwVer4/INFINIX/X572_H5312_XOS_N/DailyBuild/B1_BOM",
    "MEMORY":["#define BOARD_ID MT6735_EVB","#define CS_PART_NUMBER[0] H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1] 16EMCP16_EL3DT527","#define CS_PART_NUMBER[2] KMQE10013M_B318"],
    "TO_MAIL_LIST":["haobin.zhang@reallytek.com","zhanyang.duan@reallytek.com","ruanjianceshibu@reallytek.com"],
    "CC_MAIL_LIST":["yuanchun.yao@reallytek.com","ptyfbgxb@reallytek.com","ptyfbptrjb@reallytek.com","ruanjianyibu@reallytek.com","ruanjianxiangmuguanlibu@reallytek.com","yingjianbuceshi@reallytek.com","changkun.wu@reallytek.com","yongrong.wang@reallytek.com","zhen.wang@reallytek.com","dongming.lu@reallytek.com","weicheng.wang@reallytek.com"]
}
def getInfo(pj_info):
    pj_info=pj_info
    for key in Dict.keys():
        if key==pj_info:
            return Dict[key]
