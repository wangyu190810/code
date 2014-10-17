#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: createuser.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-17
#Description: 

import torndb
import random
import datetime
def _get_connect():
    db = torndb.Connection(host="*.*.*.*",database="",user="itp_test",password="db32@#45")
    return db
def _get_time():
    return datetime.datetime.utctime()

def set_user():
    sql_user = "insert into jaina.user (username,encrypted_password,real_name,tags,intro,avatar,banner,create_ip,email,alipay_key) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    db = _get_connect()
    for info in range(1,20):
        username = "testwang"+str(info)
        email = "emailwang"+str(info)
        alipay = "alipay"+str(info)
        real_name = "testwang"+str(info)
        encrypted_password= "12341234"+str(info)
        tags = str(info)
        intro = str(info)
        avatar = str(info)
        banner = str(info)
        create_ip = "0.0.0.1"
        db.execute(sql_user,username,encrypted_password,real_name,tags,intro,avatar,banner,create_ip,email,alipay)

def set_thrall():
    db = _get_connect()
    sql_insert = " insert into thrall.user_totals (user_id,reconciliation_gold) values (%s,%s)"
    sql_select = "select id from jaina.users where username=%s"
    for info in range(1,20):
        username = "testwang"+info
        user_id = db.get(sql_select,username)
        id = user_id["id"]
        score = random.randint(1000,2000)
        db.execute(sql_insert,id,score)

if __name__ == "__main__":
    set_user()
    set_thrall()


