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
        pass

    def treaDown(self):
        pass

    def test_String(self):
        teststr = ""
        assert type(self.anthor.stringInput()) == type(teststr)

    def test_Int(self):
        testint = 1
        assert type(self.anthor.intInput()) == type(testint)

    def test_staticStr(self):
        staticString = ""
        assert type(self.anthor.staticString()) == type(staticString)

if __name__ == "__main__":
    unittest.main()

