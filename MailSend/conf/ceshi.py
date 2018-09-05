#!/usr/bin/python

Dict = {
    "PROJECT_NAME" : "E31",
    "PLATFORM":"MT6737_N",
    "XML_NAME":"E31_H375_India",
    "VERSION_BASE":"i3",
    "SNAPSHOT_DIRECTORY":"E31_release_tag",
    "BASE_URL":"ssh://192.168.10.40:29418/MT6737_N/manifest",
    "MODEM":"git clone ssh://192.168.10.40:29418/RLK6737T_65_N_MOLY.LR9.W1444.MD.LWTG.MP.V110.5",
    "BRANCH_NAME":"E31_H375_India",
    "PROJECT_COMPLIE":"e31_h375_a1",
    "BASE_PATH":"/mnt/SwVerTemp/E31/E31-project",
    "MEMORY":["#define CS_PART_NUMBER[0]       H9TQ17ABJTMCUR_KUM","#define CS_PART_NUMBER[1]       KMQ820013M_B419",],
    "TO_MAIL_LIST":[],
    "CC_MAIL_LIST":["wei.liu2@reallytek.com"]}

def getInfo(pj_info):
        pj_info=pj_info
        for key in Dict.keys():
                if key==pj_info:
                        return Dict[key]


