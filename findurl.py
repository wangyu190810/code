#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: findurl.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-17
#Description: 

stat_str="<a href='http:/www.a.com'>xx</a>ffff <a href='http://www.b.com'>yyyy</a>" 
i = 1
while True:

    if stat_str.find(r"href='") is -1:
        break
    stat = stat_str.find(r"href='")
    end = stat_str.find(r"'>")
    end_str = stat_str[stat+6:end]
    stat_str = stat_str[end+2:]
    print end_str

    
