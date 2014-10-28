#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: register.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-09-11
#Description: 

import urllib2,urllib

data = {"username":"wanggyu","email":"wangyu@qq.com","password":'wangyu'}

f = urllib2.urlopen(
        url = "http://192.168.2.7:9090/user/",
        data = urllib.urlencode(data),
        )

print f.read()


