# coding: utf-8

import requests
import json
import csv
from bs4 import BeautifulSoup

url = "http://taqm.epa.gov.tw/taqm/tw/Pm25Index.aspx"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
for item in soup.select('.jTip'):#.jTip#Keelung
   print item.get('jtitle')
   decodejson = json.loads(item.get('jtitle'))
   data = [[decodejson['SiteKey'], decodejson['FPMI'], decodejson['PM25_AVG'], decodejson['PM25'], decodejson['PSI'], decodejson['PM10_AVG'],decodejson['PM10'],decodejson['O3']]]
   f = open(decodejson['SiteKey']+".csv",'ab')
   w = csv.writer(f)  
   w.writerows(data)  
   f.close() 
