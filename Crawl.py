#使用python3.5.1 抓取及時空氣指標 並儲存
#programmer:張弘瑜
#date:2016/05/21

import csv
import json
import requests
from bs4 import BeautifulSoup

url = "http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
decodejson = json.loads(soup.text)
for i in range(1,len(decodejson)):
   CatchData = [[decodejson[i]['County'], decodejson[i]['SiteName'],decodejson[i]['PSI'],decodejson[i]['MajorPollutant'],decodejson[i]['Status']
                  ,decodejson[i]['SO2'],decodejson[i]['CO'],decodejson[i]['O3'],decodejson[i]['PM10'],decodejson[i]['PM2.5']
                 ,decodejson[i]['NO2'],decodejson[i]['FPMI'],decodejson[i]['NOx'],decodejson[i]['NO'],decodejson[i]['PublishTime']]]
   FControl = open("Data/"+decodejson[i]['County']+".csv",'a',encoding='utf-8', newline='')#a:append newline='' 可以免去多一行的困擾
   w = csv.writer(FControl)  
   w.writerows(CatchData)  
FControl.close() 
