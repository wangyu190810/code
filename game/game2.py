#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: game2.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-15
#Description: 

"""一个关于随机数猜测的游戏 """

from random import randint

#随机数产生
def Rint():
    while True:
        rint = randint(0000,9999)

        list_rint = list(str(rint))
#        print list_rint
        if len(list_rint) == 4:
            if (list_rint[0] not in (list_rint[1]+list_rint[2]+list_rint[3])) and (list_rint[1] not in (list_rint[2]+list_rint[3])) and (list_rint[2] not in list_rint[3]):
                break
#                print list_rint
    return list_rint

#输入猜测数字
def Cheel():
    while True:
        try:
            cheelint = int(raw_input("请输入猜测值4位整数:"))
            if len(str(cheelint)) == 3:
                cheelint = "0"+str(cheelint)
            return str(cheelint)
            break
        except ValueError:
            print "请输入数字"

def main():
    rint = Rint()
    while True:
        cheel = list(Cheel())
        i=0
        j=0
        h=0
        print cheel
        if rint[0] is cheel[0]:
            i = i+1
        else:
            j = j+1
        if rint[1] is cheel[1]:
            i = i+1
        else:
            j= j+1
        if rint[2] is cheel[2]:
            i = i+1
        else:
            j = j+1
        if rint[3] is cheel[3]:
            i = i+1
        else:
            j = j+1
        if rint[0] in cheel:
            h=h+1
        if rint[1] in cheel:
            h=h+1
        if rint[2] in cheel:
            h=h+1
        if rint[3] in cheel:
            h=h+1
        if i == 4:
            print i,"A"
            print "you win"
            break
        elif i == 3 and j == 1:
            print i,"A",j,"B"
        elif h-i == 0:
            print i,"A",j,"B"
        else:
            print i,"A",j,"B",h-i,"C"

if __name__ == "__main__":
    main()


