# coding: utf-8
#抓取及時空氣指標
#programmer:張弘瑜
#date:2016/05/15
import csv
import json
import time
import requests
from bs4 import BeautifulSoup

url = "http://taqm.epa.gov.tw/taqm/tw/Pm25Index.aspx"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")#分析Html
print "Crawl Data at : " + time.strftime("%Y/%m/%d %H:%M:%S") #抓取資料的時間

for item in soup.select('.jTip'):#.jTip class
   decodejson = json.loads(item.get('jtitle'))
   CatchData = [[decodejson['SiteKey'], decodejson['FPMI'], decodejson['PM25_AVG'], decodejson['PM25'], decodejson['PSI'],\
            decodejson['PM10_AVG'],decodejson['PM10'],decodejson['O3'],time.strftime("%Y/%m/%d %H:%M:%S")]]
   FControl = open("data/"+decodejson['SiteKey']+".csv",'ab')#a:append b:binary 可以免去多一行的困擾
   w = csv.writer(FControl)  
   w.writerows(CatchData)  
FControl.close() 
