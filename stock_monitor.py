# coding: utf-8
'''
Created on 2018年7月28日

@author: guimaizi
'''
import json,time,datetime,smtplib
import tushare as ts
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler
class stock_monitor:
    def __init__(self):
        #股价监测
        self.lists=[]
    def start(self):
        try:
            while True:
                try:
                    times = datetime.datetime.now()
                    if times.hour in [9,10,11,13,14,16]:
                        #返回配置文件信息
                        with open(r"stock_list.json",'r') as load_f:
                            load_dict = json.load(load_f)
                        for i in load_dict['stock_list']:
                            if i not in self.lists:
                                self.mains(i)
                        time.sleep(15)
                    elif times.hour>14:
                        self.lists=[]
                        return 1
                    else:
                        time.sleep(80)
                except:continue
        except Exception as e:
            print(e)
            
    def mains(self,stock_code):
        print(stock_code)
        df = ts.get_realtime_quotes(stock_code) #Single stock symbol
        dfs = ts.get_stock_basics()
        data=str(df[['name','pre_close','price','amount']]).split()
        money=int(float(data[-1]))
        if int(money)>5:
            Amount=round(money/10000,0)*10000
        else:
            Amount=money
        change=round((float(data[7])-float(data[6]))/float(data[6])*100,2)
        if change>3 or change<-3:
            tests='股票: %s 当前价格:  %s ,涨跌幅: %%%s ,成交量:  %s,时间: %s'%(data[5],data[7],change,self.to_chinese(int(Amount)),datetime.datetime.now())
            print(tests)
            self.send(str(tests))
            self.lists.append(stock_code)
        #totals=(dfs.ix[stock_code]['totals'])
        #print(float(data[7])*totals)
    def send(self,texter):
        #text=','.join(texter)
        msg = MIMEText(texter)
        msg["Subject"] = "股票监控"
        msg["From"] = '1642629605@qq.com'
        msg["To"] = '635713319@qq.com'
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login('1642629605@qq.com', 'xiuqtothwbrpbeee')
            s.sendmail('1642629605@qq.com', '635713319@qq.com', msg.as_string())
            s.quit()
            print("Success!")
        except Exception as e:
            print(e)
    def to_chinese(self,number):
        """ convert integer to Chinese numeral """
        chinese_numeral_dict = {
            '0': '零',
            '1': '一',
            '2': '二',
            '3': '三',
            '4': '四',
            '5': '五',
            '6': '六',
            '7': '七',
            '8': '八',
            '9': '九'
        }
        chinese_unit_map = [('', '十', '百', '千'),
                            ('万', '十万', '百万', '千万'),
                            ('亿', '十亿', '百亿', '千亿'),
                            ('兆', '十兆', '百兆', '千兆'),
                            ('吉', '十吉', '百吉', '千吉')]
        chinese_unit_sep = ['万', '亿', '兆', '吉']
        reversed_n_string = reversed(str(number))
        result_lst = []
        unit = 0
        for integer in reversed_n_string:
            if integer is not '0':
                result_lst.append(chinese_unit_map[unit // 4][unit % 4])
                result_lst.append(chinese_numeral_dict[integer])
                unit += 1
            else:
                if result_lst and result_lst[-1] != '零':
                    result_lst.append('零')
                unit += 1
        result_lst.reverse()
        if result_lst[-1] is '零':
            result_lst.pop()
        result_lst = list(''.join(result_lst))
        for unit_sep in chinese_unit_sep:
            flag = result_lst.count(unit_sep)
            while flag > 1:
                result_lst.pop(result_lst.index(unit_sep))
                flag -= 1
        return ''.join(result_lst)

if __name__=='__main__':
    itme=stock_monitor()
    itme.start()
    '''
    scheduler = BlockingScheduler()
    scheduler.add_job(itme.start, 'cron', day_of_week='0-6', hour=16, minute=31)
    scheduler.start()
    '''