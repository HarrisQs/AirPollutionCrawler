#!/bin/bash
export  PATH=/bin:/sbin:/usr/bin:/usr/sbin
cd /home/harris/Desktop/PSI_Crawler
startd=$(date);
echo "$startd Update Data"
/usr/bin/git add .
/usr/bin/git commit -m "$startd Update Data"
/usr/bin/git push
