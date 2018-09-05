#!/bin/bash
LAST_SNAPSHOT=$1
CURRENT_SNAPSHOT=$2
PATHROOT=`pwd`
repo diffmanifests ${LAST_SNAPSHOT} ${CURRENT_SNAPSHOT} | awk '{if($3~/^from$/ && $2~/^changed$/ && $5~/^to$/ || $3~/^revision$/ && $2~/^at$/)print}' | awk '{print $1,$4,$6}' > pro_cm
sed -i 's/refs\/tags\///g' pro_cm
while read line
      do
       t1=`echo "$line" | awk  '{print $1}'`
       t2=`echo "$line" | awk  '{print $2}'`
       t3=`echo "$line" | awk  '{print $3}'`
       echo $t1
       echo $t2
       echo $t3
       cd $t1
       if [ !  -d ".git"  ];then
       cd ${PATHROOT}
       continue
       fi
       if [ ! -n "$t3" ];then
       echo $t1 >>${PATHROOT}/log.txt
       git log  ${t2} -n1  --pretty="%an|[%h] %s" | grep -v "Merge" | grep -v "J.*LY-0" | awk -F\| '{printf("%-15s\t%s\n",$1, $2) }' >> ${PATHROOT}/log.txt
       else
       echo $t1 >>${PATHROOT}/log.txt
       git log  ${t2}..${t3} --pretty="%an|[%h] %s" | grep -v "Merge" | grep -v "J.*LY-0" | awk -F\| '{printf("%-15s\t%s\n",$1, $2) }' >> ${PATHROOT}/log.txt
       if [ ${PIPESTATUS[0]} -ne 0 ];then
       git log  ${t3} -n1  --pretty="%an|[%h] %s" | grep -v "Merge" | grep -v "J.*LY-0" | awk -F\| '{printf("%-15s\t%s\n",$1, $2) }' >> ${PATHROOT}/log.txt
       fi
       fi
       cd ${PATHROOT}
done < pro_cm
#sort -b -f -d -u ${PATHROOT}/log.txt -o ${PATHROOT}/log.txt