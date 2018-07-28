# coding: utf-8
'''
Created on 2018年7月28日

@author: guimaizi
'''
import json
class stock_monitor:
    def __init__(self):
        #股价监测
        pass
    def read_config(self):
        #返回配置文件信息
        with open(r"stock_list.json",'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict