#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: output_email.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-28
#Description: 

import torndb

db = torndb.Connection(host="localhost",database="arthas",user="root",password="")
sql = "select email from users"
emails = db.query(sql)
emailfile = open("email.csv","w")
for email in emails:
    emailfile.write(str(email["email"]))
    emailfile.write("\n")

emailfile.close()

