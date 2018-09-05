#!/bin/bash
#Transsion Top Secret

# generate brief statistics report about gerrit sshd_log
# 1           2            3      4        5   6         7                                                                    8   9     10
#                                 session  username accountid cmd                                                             wait exec status
# [2016-08-25 00:53:18,794 +0800] 49af7336 scm a/1000000 git-upload-pack./MTK6755/frameworks/base/packages/CaptivePortalLogin 0ms 526ms killed

sshdlog="$1"

firstline=$(head -1 "$sshdlog")
lastline=$(tail -1 "$sshdlog")
starttime="${firstline:1:19}"
endtime="${lastline:1:19}"

usernum=$(cat "$sshdlog"|tr -s ' '|cut -d ' ' -f5|sort|uniq|wc -l)
sessionnum=$(cat "$sshdlog"|tr -s ' '|cut -d ' ' -f4|sort|uniq|wc -l)
waitlist=$(grep 'git-' "$sshdlog"|tr -s ' '|cut -d ' ' -f8)
execlist=$(grep 'git-' "$sshdlog"|tr -s ' '|cut -d ' ' -f9)

runseconds=$(python -c "from datetime import datetime; a = datetime.strptime('$starttime', '%Y-%m-%d %H:%M:%S'); b = datetime.strptime('$endtime', '%Y-%m-%d %H:%M:%S'); print int((b-a).total_seconds())")


function addall(){
    local args="$1"
python - $args <<EOF
import sys
i = 0.0
for line in open(sys.argv[1]):
    i = i + float(line.strip().strip('ms'))
    #print line
    #print i
print "%.f" % i
EOF
}

totalwaitms=$(addall <(echo "$waitlist"))
totalexecms=$(addall <(echo "$execlist"))

totalwaits=$((totalwaitms/1000))
totalexecs=$((totalexecms/1000))
gittransactnum=$(echo "$waitlist"|wc -l)

averagewaitms=$((totalwaits * 1000 / gittransactnum))
averageexecms=$((totalexecs * 1000 / gittransactnum))

echo "gerrit runs for $runseconds seconds, $gittransactnum git transactions, user number $usernum, session number $sessionnum"
echo "total wait time $totalwaits seconds, total exec time $totalexecs seconds"
echo "average wait time $averagewaitms ms, average exec time $averageexecms ms"
