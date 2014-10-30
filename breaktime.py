#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: breaktime.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-30
#Description: 

import time

def start(fun):
    print "start"
    def end():
#        time.sleep(10)
        print "1234" 
        print fun() 
        return 0
    return end
def wo(fun):
    print "end"
    def you():
        print "0987"
        print fun()
        return 0
    return you


    
@start
@wo
def test():
    a = "asdasdf"
    return a

#@start
#def app():
#    a = "12341234"
#    return a
#
if __name__ == "__main__":
    test()
#    app()
