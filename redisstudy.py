#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: redisstudy.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-16
#Description: 

import redis
r = redis.StrictRedis(host="127.0.0.1", port=6379,db=1)
r.set("foo","bar")
r.get("foo")



