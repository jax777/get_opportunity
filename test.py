# coding: utf-8
'''
Created on 2018年7月27日

@author: guimaizi
'''
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def job():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=9, minute=20)
scheduler.start()