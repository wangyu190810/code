#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: yieldtest.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-31
#Description: 
"""yield实现，和python的一些内置函数"""
def test():
    a = []
    for i in range(10):
        yield i
cc = []
ff=test()
cc = ff
print ff
print cc
for c in cc:
    print c
class FunctionalList:
    '''一个列表的封装类，实现了一些额外的函数式
    方法，例如head, tail, init, last, drop和take。'''
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        # 如果键的类型或值不合法，列表会返回异常
        return self.values[key]
    def __setitem__(self, key, value):
        self.values[key] = value
    def __delitem__(self, key):
        del self.values[key]
    def __iter__(self):
        return iter(self.values)
    def __reversed__(self):
        return reversed(self.values)
    def append(self, value):
        self.values.append(value)
    def head(self):
        # 取得第一个元素
        return self.values[0]
    def tail(self):
        # 取得除第一个元素外的所有元素
        return self.valuse[1:]
    def init(self):
        # 取得除最后一个元素外的所有元素
        return self.values[:-1]
    def last(self):
        # 取得最后一个元素
        return self.values[-1]
    def drop(self, n):
        # 取得除前n个元素外的所有元素
        return self.values[n:]
    def take(self, n):
        # 取得前n个元素
        return self.values[:n]
class Fun(FunctionalList):
    def __init__(self,aaa=None):
        self.aaa = aaa
    def test(self):
        print self.aaa
        return self.aaa
if __name__ == "__main__":
    fun = FunctionalList()
    print  fun.__len__()
#    fun.__setitem__(1,"12")
#    print fun.__getitem__(12)
#    print fun.__item__(12)
#    fun.__delitem__(12)
    fun.append("123123")
    fun.append("123123")
    fun.append("123123")
    fun.append("123123")
    fun.head()
    fun.drop(2)
    fun2 = Fun(1234123123)
    fun2.test()
