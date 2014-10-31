#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: lamdbatest.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-31
#Description: 

a = lambda x : x*2
print a(123)

print (lambda a : a.split(","))("123,412,34")
print (lambda a : a.strip())("   123  ,412  ,34  ")

ff = lambda x : len(x)

