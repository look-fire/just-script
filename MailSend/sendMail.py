#!/usr/bin/python
# coding: utf-8 
import smtplib
import os
import sys
import time
import readline
import commands
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from time import strftime, localtime
import time
from pyExcelerator import *
c_path=os.getcwd()
sys.path.append('%s/conf/'%c_path)


class Mail():
    
    # 修改默认的编码格式    
    default_encoding = 'utf-8'
    if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)
    
    # get parameter from conf.py
    def getConf(self,pj_conf=''):
        if pj_conf.strip()=='':
            list_conf=os.listdir("%s/conf"%c_path)
            print "project list: %s"%list_conf
            pj_conf=raw_input("please input the Porject:")
        conf=__import__(pj_conf)
        self.project=conf.getInfo("PROJECT_NAME")
        self.project_jira_url=conf.getInfo("PROJECT_JIRA_URL")
        if self.project_jira_url is None:
            self.project_jira_url="http://192.168.1.85:8080/secure/BrowseProjects.jspa#all"
        self.build_mode=conf.getInfo("BUILD_MODE")
        if self.build_mode is None:
            self.build_mode="user"
        self.platform=conf.getInfo("PLATFORM")
        self.xml_name=conf.getInfo("XML_NAME")
        self.version_base=conf.getInfo("VERSION_BASE")
        self.snapshot_dir=conf.getInfo("SNAPSHOT_DIRECTORY")
        self.base_url=conf.getInfo("BASE_URL")
        self.modem=conf.getInfo("MODEM")
        self.branch_name=conf.getInfo("BRANCH_NAME")
        self.complie=conf.getInfo("PROJECT_COMPLIE")
        self.make_mode=conf.getInfo("MAKE_MODE")
        if self.make_mode is None:
            self.complie_key="source rlk_setenv.sh %s %s && make -j24 2>&1 | tee build.log"%(self.complie,self.build_mode)
        else:
            self.complie_key="./mk %s user new"%(self.complie)
        self.base_dir=conf.getInfo("BASE_PATH")    
        self.memory_list=conf.getInfo("MEMORY")
        self.to_mail_list=conf.getInfo("TO_MAIL_LIST")
        self.cc_mail_list=conf.getInfo("CC_MAIL_LIST")

    # get parameter from version_dir 
    def getVersionInfo(self,path='',release_for=''):
        if path.strip()=='':
            if not os.path.isdir(self.base_dir):
                print "can not find %s!!,Please check the server is mounted"%base_dir
            cmd='ls -t %s' %self.base_dir
            values=commands.getoutput(cmd)
            temp=values.split("\n")
            for i in range(len(temp)):
                print '%s: %s'%(i+1,temp[i])

            number_dir = int(raw_input("choose target_dir for send mail: "))
            release_for = raw_input("Version release for: ")
            self.date_dir=temp[number_dir-1]
            self.target_dir=self.base_dir+"/"+self.date_dir
        else:
            self.target_dir=path
        self.win_temp_dir=self.target_dir.replace("/","\\")
        self.win_dir=self.win_temp_dir.replace("mnt","192.168.1.75")
        print "The target_dir is : %s"%self.target_dir
        version_cmd='basename "%s"/%s*.zip | sed "s/.zip//g" '%(self.target_dir,self.version_base)
        self.version_number=commands.getoutput(version_cmd)
        print "The versionNumber is : %s" %self.version_number
        snap_cmd='ls "%s" | grep -v .*-CLEAN-SNAPSHOT | grep .*.xml'%self.target_dir
        self.snap=commands.getoutput(snap_cmd)
        print "The snap_XML is : %s"%self.snap
        change_log=self.target_dir+'/log.txt'
        if not os.path.isfile(change_log):
            print "please check if exits ChangLog!"
            self.change_log=""
        else:
            self.change_log=change_log
            print "The changeLog path is : %s"%change_log
        self.log_list=self.getLogList(self.change_log)
        self.release_for=release_for

    def getLogList(self,change_log):
        log_List = []
        if not os.path.isfile(change_log):
            print "please check if exits ChangLog!"
        else :
            result=open(change_log)
            lines=result.readlines()
            result.close
            for line in lines:
                log_List.append(line)
            return log_List

    def getDaulftBorder(self):
        borders = Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        return borders

    def getReleaseNoteTitleStyle(self, color):
        fnt = Font()
        fnt.name = 'Arial'
        fnt.colour_index = 0
        fnt.bold = True
        fnt.height=260
        borders=self.getDaulftBorder()
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

    def getHeadTitleItemStyle(self):
        fnt = Font()
        fnt.name = 'Arial'
        fnt.colour_index = 0
        fnt.bold = True
        fnt.height=200
        borders=self.getDaulftBorder()
        al = Alignment()
        al.horz = Alignment.HORZ_LEFT
        al.vert = Alignment.VERT_CENTER
        style = XFStyle()
        style.font = fnt
        style.borders = borders
        style.alignment = al
        return style

    def getHeadTitleItemInfoStyle(self, big=False, bold=False, center=False):
        fnt = Font()
        fnt.name = u'Times New Roman'
        fnt.colour_index = 0
        if big:
            fnt.height=250
        else:
            fnt.height=200
        fnt.bold = bold
        borders=self.getDaulftBorder()
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

    def saveExcel(self,savePath):
        workbook = Workbook()
        maxColumn = 16
        worksheet = workbook.add_sheet("releasenote")
        worksheet.write_merge(0, 1, 0, maxColumn, 'RELEASE NOTE' , self.getReleaseNoteTitleStyle(17))
        worksheet.write_merge(2,2,0,8,'Project: %s'%self.project,self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(2,2,8,16,'Platform: %s'%self.platform,self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(3,3,0,maxColumn,'Version code address:',self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(4,4,0,maxColumn,'repo init -u %s -m %s.xml'%(self.base_url,self.xml_name),self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(5,5,0,maxColumn,'Modem:',self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(6,6,0,maxColumn,'git clone %s'%self.modem,self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(7,7,0,maxColumn,'branch : %s'%self.branch_name,self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(8,8,0,maxColumn,'version_number: %s'%self.version_number,self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(9,9,0,maxColumn,'snap: %s/%s'%(self.snapshot_dir,self.snap),self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(10,10,0,maxColumn,u'版本路径：%s'%self.win_dir,self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(11,11,0,maxColumn,u'Compile Key：%s'%(self.complie),self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(12,12,0,maxColumn,u'Checksum Version：1604',self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(13,13,0,maxColumn,u'Custom Memory:',self.getHeadTitleItemInfoStyle())
        CurrentC=13
        for i in range(len(self.memory_list)):
            CurrentC += 1
            worksheet.write_merge(CurrentC,CurrentC,0,maxColumn,'#define &nbsp %s'%self.memory_list[i],self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(CurrentC+1,CurrentC+1,0,maxColumn,u'release for：【%s】 %s'%(self.project,self.release_for),self.getHeadTitleItemInfoStyle())
        worksheet.write_merge(CurrentC+2,CurrentC+2,0,maxColumn,u'Change Log : ',self.getHeadTitleItemInfoStyle())
        CurrentC=CurrentC+2
        if self.log_list:
            for i in range(len(self.log_list)):
                CurrentC += 1
                if self.log_list[i].find("]")==-1:
                    worksheet.write_merge(CurrentC,CurrentC,0,maxColumn,u'库名：%s'%self.log_list[i].decode('utf-8'),self.getHeadTitleItemStyle())
                else:
                    username=self.log_list[i].split("[")[0]
                    comment=self.log_list[i].split("[",1)[1]
                    worksheet.write_merge(CurrentC,CurrentC,0,maxColumn,u'%s [%s'%(username,comment),self.getHeadTitleItemInfoStyle())
        else:
            worksheet.write_merge(CurrentC,CurrentC,0,maxColumn,'No Change Log',self.getHeadTitleItemStyle())
        workbook.save('%s/ReleaseNote.xls'%savePath)
    
    def getMailList(self,names):
        name_list = names.split(",")
        mail_list = []
        for i in name_list:
            item = i + "@reallytek.com"
            mail_list.append(item)
        return mail_list
        
    def sendMail(self,to_mail):
        from_mail='scmmail@reallytek.com'
        if to_mail is None or not to_mail.strip():
            to_mail = self.to_mail_list + self.cc_mail_list
            To = self.to_mail_list
            Cc = self.cc_mail_list
        else:
            to_mail = self.getMailList(to_mail)
            To = to_mail
            Cc = [""]
        print "收件人有以下这些：\n %s"%to_mail
        msg=MIMEMultipart()
        msg['Date'] = strftime("%a, %d %b %Y %T", localtime()) + ' +0800'
        msg['From']=from_mail
        msg['To']=','.join(To)
        msg['CC']=','.join(Cc)
        msg['Subject']='【SCM release版本】【%s】%s--------%s'%(self.project,self.release_for,self.version_number)
        html = '<html xmlns="http://www.w3.org/1999/xhtml">'
        html += '<head>'
        html += '<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />'
        html += '<style type="text/css">'
        html += 'body {font-family:arial; font-size:10pt;}'
        html += 'td {font-family:arial; font-size:10pt;}'
        html += '</style>'
        html += '</head>'
        html += '<body><center>'
        html += '<table border="1" cellspacing="0" cellpadding="2"  width="1000">'
        html += '<tr><td colspan="2" ><p align="center" style="font-size:30px">Release  Note</p> </td></tr>'
        html += '<tr><td><p align="left" style="font-size:15px">项目名：<a href="%s">%s </a></p></td><td><p align="left" style="font-size:15px"> 平台: %s</p></td></tr>'%(self.project_jira_url,self.project,self.platform)
        html += '<tr><td colspan="2"><p>原始版本路径 ：<font color=blue> repo init -u %s -m %s.xml</font><br>'%(self.base_url,self.xml_name)
        html += 'MODEM:  <font color=blue> git clone %s</font></p></td></tr>'%self.modem
        html += '<tr><td colspan="2">branch: %s</td></tr>'%self.branch_name
        html += '<tr><td colspan="2">快照: %s/%s</td></tr>'%(self.snapshot_dir,self.snap)
        html += '<tr><td colspan="2"><p><font color="red">版本号：%s</font></p></td></tr>'%self.version_number
        print "self.win_dir:%s" %self.win_dir
        html += '<tr><td colspan="2"><p>路径：<a href="file:\%s"> \\%s </a></p></td></tr>'%(self.win_dir,self.win_dir)
        html += '<tr><td colspan="2"><p>编译命令：%s </p></td></tr>' %(self.complie_key)
        html += '<tr><td colspan="2"><p>Checksum Version：v5.1540.00</p></td></tr>'
        html += '<tr><td colspan="2"><p>兼容Memory: </p></td></tr>'
        for i in range(len(self.memory_list)):
            html +=  '<tr><td colspan="2">%s</td></tr>'%(self.memory_list[i])
        html += '<tr><td colspan="2"><p><font color="red">release 目的：【%s】 %s</font></p></td></tr>'%(self.project,self.release_for)
        html += '<tr><td colspan="2"><p>Change Log : </p></td></tr>'
        #change_log
        if self.log_list:
            for i in range(len(self.log_list)):
                if self.log_list[i].find("]")==-1:
                    html +=  '<tr><td width="400"><font color="#0000FF">库名：%s</td><td><b>&nbsp</b></td></tr>'%(self.log_list[i])
                else:
                    username=self.log_list[i].split("[")[0]
                    comment=self.log_list[i].split("[",1)[1]
                    html +=  '<tr><td width="150" bgcolor="green">%s&nbsp&nbsp</td><td><b>[%s</b></td></tr>'%(username,comment)
        else :
            html +=  '<tr><td width="150">No Change Log</td></tr>'
        html += '</table></center>'
        # SIGHTURE
        html += '<br /> <br /> <br />'
        html += '<font  face=verdana size="3" >SCM TEAM</font><br>'
        html += '<font color=gray face=verdana size="2" > R&D Section 1 SW Dept. SCM Team | 研发一部 软件开发部 SCM组   <br>'
        html += 'Email: scmmail@reallytek.com <br>'
        html += '<br>'
        html += 'Research & Development Center | 研发中心 TRANSSION HOLDINGS | 传音控股<br>'
        html += 'Web: www.transsion.com Postcode: 201203 <br>'
        html += '地址: 上海市浦东新区张江科技园郭守敬路433号1号楼 <br>'
        html += 'Add: No.1 Building, No.433 Guoshoujing Road, Pudong District'
        html += '</body>'
        html += '</html>'
        html_part = MIMEText(html,'html','utf-8')
        #encode rs.encode_base64(html_part)
        msg.attach(html_part)
        if self.change_log.strip()!="":
            att_log=open(self.change_log,'rb')
            att = MIMEText(att_log.read() , 'base64')
            att['Content-Type']='application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="release_note.txt"'
            msg.attach(att)
        else:
            print "have no Change Log"
        server=smtplib.SMTP('mail.reallytek.com')
        server.docmd('ehlo','scmmail@reallytek.com')
        server.login('scmmail@reallytek.com','Reallytek#')
        server.sendmail(from_mail,to_mail,msg.as_string())
        print 'send Email Success!'
        server.quit()
        #save Excel
        self.saveExcel(self.target_dir)

if __name__=='__main__':
    M=Mail()
    base_Dir=''
    project=''
    release_For=u'内测软件'
    to_mail=''
    if len(sys.argv)==3:
        project=sys.argv[1]
        base_Dir=sys.argv[2]
    if len(sys.argv)==4:
        project=sys.argv[1]
        base_Dir=sys.argv[2]
        release_For=sys.argv[3]
    if len(sys.argv)==5:
        project=sys.argv[1]
        base_Dir=sys.argv[2]
        release_For=sys.argv[3]
        to_mail=sys.argv[4]
    M.getConf(project)
    M.getVersionInfo(base_Dir,release_For)
    if len(sys.argv)==1:
        print "----不写收件人默认发送配置文件里的所有人;发送给自己可以写自己的名字例如 dongming.lu---- \n"
        to_mail=raw_input("to_mail is:")
    M.sendMail(to_mail)
