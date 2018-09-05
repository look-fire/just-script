#!/usr/bin/python
# coding: utf-8
import sys
import os
sys.path.append("/ci/paramiko")
import paramiko
import threading
from pyExcelerator import *
def ssh2(ip,username,passwd,cmd):
    serverInfoDict={}
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        print 'CONNECT %s\tSUCCESS\n'%(ip)
        outList = []
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            stdin.write("Y")   #简单交互，输入 ‘Y’ 
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print o,
                outList.append(o)
            serverInfoDict[ip]=outList
        ssh.close()
    except :
        print '%s\tError\n'%(ip)
    return serverInfoDict
def getIpList(path):
    if os.path.isfile(path):
        output=open(path)
        ipList=output.readlines()
    else:
        print "%s not found."%path
    return ipList;

def getReleaseNoteTitleStyle(color):
    fnt = Font()
    fnt.name = 'Arial'
    fnt.colour_index = 0
    fnt.bold = True
    fnt.height=260
    borders=getDaulftBorder()
    al = Alignment()
    al.horz = Alignment.HORZ_CENTER
    al.vert = Alignment.VERT_CENTER
    pattern = Pattern()
    pattern.pattern=1
    pattern.pattern_fore_colour=color
    pattern.pattern_back_colour=color #17, 5
    fnt.height=280
    #fnt.height=220
    style = XFStyle()
    style.font = fnt
    style.borders = borders
    style.alignment = al
    style.pattern=pattern
    return style

def getHeadTitleItemInfoStyle(big=False, bold=False, center=False):
    fnt = Font()
    fnt.name = u'Times New Roman'
    fnt.colour_index = 0
    if big:
            fnt.height=250
    else:
            fnt.height=200
    fnt.bold = bold
    borders=getDaulftBorder()
    al = Alignment()
    if center:
            al.horz = Alignment.HORZ_CENTER
    else:
            al.horz = Alignment.HORZ_LEFT
    al.vert = Alignment.VERT_CENTER
    style = XFStyle()
    style.font = fnt
    style.borders = borders
    style.alignment = al
    return style

def getDaulftBorder():
    borders = Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    return borders 
 
def mkExcel(serverInfoDict):
    print "start mkExcel"
    workbook = Workbook()
    maxColumn = 17
    maxRow = 14
    worksheet = workbook.add_sheet("ServerInfo")
    worksheet.write_merge(0, 1, 0, maxColumn, 'SERVER INFO' , getReleaseNoteTitleStyle(17))
    worksheet.write_merge(2, 2, 0, 1 , 'IP' , getHeadTitleItemInfoStyle())
    worksheet.write_merge(2, 2, 2, 3 , 'AVAIL_DISK' , getHeadTitleItemInfoStyle())
    worksheet.write_merge(2, 2, 4, 5 , 'MENBERS' , getHeadTitleItemInfoStyle())
    CCol = 3
    for k in serverInfoDict.keys():
        worksheet.write_merge(CCol, CCol, 0, 1 , k , getHeadTitleItemInfoStyle())
        for i in range(2):
            worksheet.write_merge(CCol+i, CCol+i, 2, 3, serverInfoDict[k][i] , getHeadTitleItemInfoStyle())
        for i in range(len(serverInfoDict[k])-2):
            worksheet.write_merge(CCol+i, CCol+i, 4, 5, serverInfoDict[k][i+2] , getHeadTitleItemInfoStyle())
        CCol = CCol+len(serverInfoDict[k])
    workbook.save('ServerInfo.xls')

if __name__=='__main__':
    #cmd_cat="cat /home/user*/.gitconfig|grep name|cut -d " " -f3"
    #print cmd_cat
    ipFile="ip.txt"
    cmd = ['echo "当前剩余空间："','df -h /|tail -1|tr -s " "|cut -d " " -f4','echo "服务器用户名单："','cat /home/user*/.gitconfig|grep -aoE "name[ ]*=.*" | cut -d " " -f3']
    username = "user1"
    passwd = "user1"   
    threads = []
    ipList=getIpList(ipFile)
    #ipList = ['192.168.10.17','192.168.10.19','192.168.10.23','192.168.10.24','192.168.10.25','192.168.10.26','192.168.10.27','192.168.10.28','192.168.10.30','192.168.10.23','192.168.10.26','192.168.10.29','192.168.10.25','192.168.10.28','192.168.10.20']  
    print "Begin......"
    serverInfoDict={}
    for i in range(len(ipList)):
        ip = ipList[i]
        #jobs=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        #jobs.start() 
        tempDict=ssh2(ip,username,passwd,cmd)
        serverInfoDict=dict(serverInfoDict.items()+tempDict.items())
        print "------------*****-*****------------\n"
    mkExcel(serverInfoDict)
