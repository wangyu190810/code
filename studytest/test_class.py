#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: test_class.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-09
#Description: 





class TestClass:
    def app(self,ccc=None):
        if ccc is None:
            assert ccc is None
        else:
            return ccc

    def test_one(self):
        x="this"
        assert "h" in x
    def test_two(self):
        x="hello"
        assert hasattr(x,"check")
    def test_three(self):
        self.app(ccc=123)

    def test_four(self):
        self.app()

