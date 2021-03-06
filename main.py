#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from functools import reduce
from mail import Mail
import time

CODING='utf-8'
MAX=300
web='http://dean.xjtu.edu.cn/'
time_r=20
print('Now gointo circle.sleep=',time_r)

while(True):
    #print('while')
    try:
        html_text=requests.get(web,timeout=5).content.decode('utf-8','ignore')
        soup = BeautifulSoup(html_text,'html.parser')
        myattrs={'class':'xstz_list_ul'}
        tzs=soup.find_all(name='ul',attrs=myattrs)
        assert len(tzs)==2
        xytz=tzs[0]
        lis=xytz.find_all(name='li')
        hrefs1=list(map(lambda x: (x.find(name='a',attrs={'class':''}).get('href'),x.find(name='a',attrs={'class':''}).text),lis))

        zhtz=tzs[1]
        lis=zhtz.find_all(name='li')
        hrefs2=list(map(lambda x: (x.find(name='a',attrs={'class':''}).get('href'),x.find(name='a',attrs={'class':''}).text),lis))
        href_list= list(hrefs1) + list(hrefs2)
        already_list=[]
        already=set([])
        m=Mail()
        with open('data.txt','r',encoding=CODING) as fi:
            x=fi.readline().strip()
            i=0
            while(x):#item at last will be remove
                if i >= MAX:
                    break
                already_list.append(x)
                x=fi.readline().strip()
                i=i+1
        already=set(already_list)
        list_new=[]
        #print(already)
        for x in href_list:
            if not (x[0] in already) :
                list_new.append(x)
                print(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())),'To add : '+x[0]+'  '+x[1])
                count_m=0
                while(not m.mailing('教务处:'+x[1],x[1]+'\n'+web+x[0])):
                    time.sleep(5)
                    count_m=count_m+1
                    if(count_m>3):
                        time.sleep(time_r)
                        raise Exception('Mailing failed 4 times,skip and try while circle again.')
        with open('data.txt','w',encoding=CODING) as fo:
            for x in list_new:
                fo.write(x[0]+'\n')
            for x in already_list:
                fo.write(x+'\n')
        time.sleep(time_r)
    except Exception as e:
        print(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())),e)

#print(len(already))
#with open('data.txt','a',encoding=CODING) as fo:
#    for x in hrefs2:
#        fo.write(x[0]+'\n')
print('Done')
#info/1096/6245.htm


