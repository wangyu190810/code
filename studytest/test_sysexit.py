#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: test_sysexit.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-09
#Description: 

import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

