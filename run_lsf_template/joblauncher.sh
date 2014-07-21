#!/bin/sh
#
# loop n-times
#
 if [ $# -ne 7 ]; then
     echo "Error - in command line arguments"
     echo " Usage: loop [eng: inj/lowb] [.450,.coll,.all,.ecoll, or nothing] [halo hor/ver] [beam: b1/b2] [queue name] [i_start] [i_stop]"
     exit 127
 fi
 
 eng=$1
 app=$2
 halo=$3
 beam=$4
 queque=$5
 i_start=$6
 i_stop=$7
 
 # queque: 8nh, 8nm


 while [ $i_start -le $i_stop ]
   do
   echo "$i_start, $i_stop"
   ./myjob $eng $app $halo $beam $queque $i_start 
   i_start=`expr $i_start + 1`
 done
