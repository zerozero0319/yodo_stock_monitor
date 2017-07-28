# -*- coding: utf-8 -*- 

from urllib.request import urlopen
import time, datetime, random

class check_yodobashi:
    url = "http://www.yodobashi.com/product/xxxxxxxxxxxxxxxxxx/"
    
    while True:
        now = datetime.datetime.today()
        
        response = urlopen(url)
        status = response.code
        html = response.read().decode('utf-8')
        
        canbuy = not '予定数の販売を終了しました' in html
        deny = 'ご使用の環境から大量のアクセスが検出されました' in html
        
        if deny == True:
            print('アクセス制限中')
            time.sleep(30)
            continue
        
        wait = random.randint(10,20)
        if canbuy == 1:
            print('買え', end=' ')
        else:
            print('ないです', end=' ')
        
        print(status, end=' ')
        print('(', now, ')', sep="")
        print(wait)
        
        time.sleep(wait)

