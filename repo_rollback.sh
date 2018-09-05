#!/bin/bash
basetimstamp=`date -d "$1" +%s`
echo $basetimstamp
for i in `repo forall -c 'echo $REPO_PATH'`
do
cd $i
  commithash=`git log --format="%h %ct" | awk '$2<="'$basetimstamp'"&&$2>a{a=$2;b=$1}END{print b}'` 
  git checkout ${commithash}
cd -
done
