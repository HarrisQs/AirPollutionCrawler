#!/bin/bash
export  PATH=/bin:/sbin:/usr/bin:/usr/sbin
cd /home/harrisqs/AirPollutionCrawler
startd=$(date);
echo "$startd Update Data"
/usr/bin/git add .
/usr/bin/git commit -m "$startd Update Data"
/usr/bin/git push
