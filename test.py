# coding: utf-8
'''
Created on 2018年7月27日

@author: guimaizi
'''
import tushare as ts

df = ts.get_realtime_quotes('601607') #Single stock symbol
data=str(df[['name','pre_close','price','time']]).split()
print(data)
dfs = ts.get_stock_basics()
totals=(dfs.ix['601607']['totals'])
print(totals)
print(float(data[7])*totals)