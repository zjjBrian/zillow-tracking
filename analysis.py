# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:33:20 2022

@author: zjjbr
"""

import pandas as pd
import glob

# find file path
filePath = "C:/Users/zjjbr/Desktop/"
fileNameActive = "zillow_active"
fileNameSold = "zillow_sold"

# initialize empty dataframes
df_active = pd.DataFrame([])
df_sold = pd.DataFrame([])

# read in active data
for f in glob.glob(filePath + fileNameActive + "*.csv"):
    active = pd.read_csv(f)
    df_active = df_active.append(active, ignore_index = True)
    
# read in sold data
for f in glob.glob(filePath + fileNameSold + "*.csv"):
    sold = pd.read_csv(f)
    df_sold = df_sold.append(sold, ignore_index = True)

df_sold['variableData'] = df_sold['variableData'].astype("string")
df_sold['soldDate'] = df_sold['variableData'].str[-12:-2]
df_sold['soldDate'] = pd.to_datetime(df_sold['soldDate'])
