# coding: utf-8
'''
Created on 2018年7月27日

@author: guimaizi
'''
import json,requests,time,datetime
def get_lunar(data):
    url = "https://www.sojson.com/open/api/lunar/json.shtml?date=%s"%(data)
    time.sleep(3)
    data_lunar = json.loads(requests.get(url).text)
    lunar_year = data_lunar['data']['lunarYear']
    lunar_month = data_lunar['data']['lunarMonth']
    lunar_day = data_lunar['data']['lunarDay']
    # print(data_lunar['data'])
    return lunar_year,lunar_month,lunar_day
print(get_lunar(2018/7/28))