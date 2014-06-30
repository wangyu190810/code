#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: post.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-29
#Description: 

import psycopg2

conn =psycopg2.connect(database="tongpao",user="postgres",password="wangyu",host="127.0.0.1",port="5432")
cur=conn.cursor()
    
cur.execute("CREATE table if not Exists test(id serial PRIMARY KEY,num integer,data varchar);")
cur.execute("insert into test(num,data)values(%s,%s)",(1,"qqaaaqq"))
cur.execute("insert into test(num,data)values(%s,%s)",(3,"qqaaaqq"))
cur.execute("insert into test(num,data)values(%s,%s)",(8,"qddqqq"))
cur.execute("insert into test(num,data)values(%s,%s)",(0,"qqqdddq"))
cur.execute("insert into test(num,data)values(%s,%s)",(8,"qqqdq"))
cur.execute("insert into test(num,data)values(%s,%s)",(9,"qqsdqq"))
cur.execute("insert into test(num,data)values(%s,%s)",(4,"qqq23q"))
cur.execute("insert into test(num,data)values(%s,%s)",(1,"23"))

cur.execute("SELECT * FROM test;")
rows=cur.fetchall()
print(rows)

for i in rows:
    print i

conn.commit()
cur.close()
conn.close()


