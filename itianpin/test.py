#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: test.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-01
#Description: 

import urllib2,urllib

data = {"ip":"::ffff:1.0.146.0"}

f=urllib2.urlopen(
        url = "http://127.0.0.1:8888",
        data = urllib.urlencode(data),
        
        )
print f.read()

