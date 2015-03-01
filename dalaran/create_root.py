#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: create_root.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-16
#Description: 

import getpass
import sys
from angel.model.user import add_new_user
from angel.model.base import conn

def set_root():
    rootname = unicode(raw_input("输入你的用户名，必须是甜品邮箱后缀："))
    if "@itianpin.com" not in rootname:
        print u"输入用户不正确"
        return

    password = getpass.getpass("输入root用户密码，不能少于12位:")

    if len(password) < 12:
        print "密码不能少于12位"
        return
    add_new_user(conn(),username=rootname,password=password,ip="100.100.100.100",is_superuser=1)
    print password
    print u"添加成功"


if __name__ == "__main__":
    set_root()


