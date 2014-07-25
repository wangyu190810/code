#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: class_anthor_test.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-24
#Description: 

import unittest
from test_class_anthor import App

class testAnthor(unittest.TestCase):

    anthor = App()

    def setUp(self):
        print "开始测试" 
        self.teststr = ""
        self.testint = 1
        self.staticString = ""

    def treaDown(self):
        print "测试结束"
        
    def test_String(self):
        print "test str"
        assert type(self.anthor.stringInput()) == type(self.teststr)

    def test_Int(self):
        print "test int"
        assert type(self.anthor.intInput()) == type(self.testint)

    def test_staticStr(self):
        print "static string"
        assert type(self.anthor.staticString()) == type(self.staticString)

if __name__ == "__main__":
    unittest.main()

