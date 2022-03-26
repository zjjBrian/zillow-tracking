# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:40:09 2022

@author: zjjbr
"""

import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

numBed = 2
numBath = 1.5
city = "orange-county-ca"
today = date.today()

## Active Listings
url1 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/".format(city,numBed,numBath)
url2 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/2_p/".format(city,numBed,numBath)
url3 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/3_p/".format(city,numBed,numBath)
url4 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/4_p/".format(city,numBed,numBath)
url5 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/5_p/".format(city,numBed,numBath)
url6 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/6_p/".format(city,numBed,numBath)
url7= "https://www.zillow.com/{}/{}-_beds/{}-_baths/7_p/".format(city,numBed,numBath)
url8 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/8_p/".format(city,numBed,numBath)
url9 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/9_p/".format(city,numBed,numBath)
url10 = "https://www.zillow.com/{}/{}-_beds/{}-_baths/10_p/".format(city,numBed,numBath)

urlList = [url1,url2,url3,url4,url5,url6,url7,url8,url9,url10]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

output = []
output = pd.DataFrame(output)
    
for url in urlList:

    soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")
    
    data = json.loads(
        soup.select_one("script[data-zrr-shared-data-key]")
        .contents[0]
        .strip("!<>-")
    )
    
    # uncomment this to print all data:
    # print(json.dumps(data, indent=4))
    
    for result in data["cat1"]["searchResults"]["listResults"]:
        df = pd.DataFrame([result])
        df['Extract Date'] = today
        output = output.append(df, ignore_index=True)


## Sold Listings        
url11 = "https://www.zillow.com/{}/sold/".format(city)
url12 = "https://www.zillow.com/{}/sold/2_p/".format(city)
url13 = "https://www.zillow.com/{}/sold/3_p/".format(city)
url14 = "https://www.zillow.com/{}/sold/4_p/".format(city)
url15 = "https://www.zillow.com/{}/sold/5_p/".format(city)
url16 = "https://www.zillow.com/{}/sold/6_p/".format(city)
url17 = "https://www.zillow.com/{}/sold/7_p/".format(city)
url18 = "https://www.zillow.com/{}/sold/8_p/".format(city)
url19 = "https://www.zillow.com/{}/sold/9_p/".format(city)
url20 = "https://www.zillow.com/{}/sold/10_p/".format(city)


urlListSold = [url11,url12,url13,url14,url15,url16,url17,url18,url19,url20]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

outputSold = []
outputSold = pd.DataFrame(outputSold)
    
for url in urlListSold:

    soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")
    
    data = json.loads(
        soup.select_one("script[data-zrr-shared-data-key]")
        .contents[0]
        .strip("!<>-")
    )
    
    # uncomment this to print all data:
    # print(json.dumps(data, indent=4))
    
    for result in data["cat1"]["searchResults"]["listResults"]:
        df = pd.DataFrame([result])
        df['Extract Date'] = today
        outputSold = outputSold.append(df, ignore_index=True)

## Save output
filePath = "C:/Users/zjjbr/Desktop/"
fileNameActive = "zillow"
fileNameSold = "zillow_sold"
fileExtension ="-{}.csv".format(today)

filePath + fileNameSold + fileExtension

output.to_csv(filePath + fileNameActive + fileExtension)
outputSold.to_csv(filePath + fileNameSold + fileExtension)



