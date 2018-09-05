#!/usr/bin/python

import os,commands
class SmbClient(object):

        def __init__(self,shareDir,username,password,ip='192.168.1.75'):
            self.shareDir = shareDir
            self.ip = ip
            self.username = username
            self.password = password
            self.time = 0
            self.NT_STATUS = "NT_STATUS_"
            self.CMDNOTFOUND = "command not found"

        def runCmd(self,command):
            command = command
            base_cmd = ['smbclient','-c']
            base_cmd.append(command)
            shareDir = '//'+self.ip+'/'+self.shareDir
            base_cmd.append(shareDir)
            base_cmd.append('-U')
            user_info = '"%s%%%s"'%(self.username,self.password)
            base_cmd.append(user_info)
            print 'start execute cmd: %s'%(' '.join(base_cmd))
            output = commands.getoutput(' '.join(base_cmd))
            status = self.checkSmbResult(output)
            if status==self.NT_STATUS:
               self.time = self.time + 1
               if self.time >= 3 :
                   print "Try again failed three times ,will exit"
                   exit()
               print "smbclient execute failed! will try again"
               self.runCmd(command)
            else:
                return output

        def checkSmbResult(self,result):
            result = result
            if self.CMDNOTFOUND in result:
                print "cmd is not right!"
                exit()
            if self.NT_STATUS in result:
                return self.NT_STATUS
           
