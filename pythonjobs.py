#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: pythonjobs.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-19
#Description: 

import urllib
import urllib2
from bs4 import BeautifulSoup
import time
f = urllib2.urlopen(
        url = "http://www.lagou.com/jobs/list_python?kd=python&spc=&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city="
        )

html = f.read()
soup = BeautifulSoup(html)
content = soup.find_all("li")
i = 0
while True:
    i = i+1
    if "clearfix" in str(content[i]):
        soup1 = BeautifulSoup(str(content[i]))
        content1 = soup1.find_all("span")
        for j in content1:
            start = str(j).find(r'">')
            end = str(j).find(r'</')
            content2 = str(j)[start+2:end]
            print content2
            
            content_start = str(j).find(r'</em>')
            content_end = str(j).find(r'</span>')
            content_content = str(j)[content_start+5:content_end]
            print content_content

        print time.sleep(1)
    print i

    if len(content) == i:
        break










