# coding: utf-8
'''
Created on 2018年7月27日

@author: guimaizi
'''
import tushare as ts

df = ts.profit_data(top=60)
df.sort('shares',ascending=False)