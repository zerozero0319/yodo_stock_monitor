# -*- coding: utf-8 -*- 

from urllib.request import urlopen
import time, datetime

class check_yodobashi:
    url = "http://www.yodobashi.com/product/xxxxxxxxxxxxxxxxxx/"
    
    while True:
        now = datetime.datetime.today()
        
        response = urlopen(url)
        status = response.code
        html = response.read().decode('utf-8')
        
        canbuy = not '予定数の販売を終了しました' in html
        
        if canbuy == 1:
            print('買え', end=' ')
        else:
            print('ないです', end=' ')
        
        print(status, end=' ')
        print('(', now, ')', sep="")
        
        time.sleep(2)

