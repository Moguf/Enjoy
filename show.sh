#!/bin/sh 

for i in `ls dp*.out`
do
    name=${i%.*}
    echo $i
    python show.py $i
    #if [ ! -e $name".mp4" ];then
    #    echo $name
    #fi
done
