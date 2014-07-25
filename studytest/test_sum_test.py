#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: test_sum_test.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-24
#Description: 

import unittest
import test_sum

class mytest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sum(self):
        self.assertEqual(test_sum.sum(1,3),4,"success")

    def test_sub(self):
        self.assertEqual(test_sum.sub(1,3),3,"Error Value")

if __name__ == "__main__":
    unittest.main()


