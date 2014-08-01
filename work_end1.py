#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: work_count.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-28
#Description: 

import MySQLdb
import sys
import time
import sqlite3
import datetime

def nowtime():
    a = datetime.datetime.now()
    daytime = str(a).split(":")
    day = str(daytime[0]).split(" ")
    return str(day[0])

def yestime():
    a = datetime.datetime.now()-datetime.timedelta(days=1)
    daytime = str(a).split(":")
    day = str(daytime[0]).split(" ")
    return str(day[0])


def filelen(title):
    aaa=len(title)
    titlelen = 40 - aaa
    print titlelen
    title = title+titlelen*""
    return title

def positive_number(number):
    if number > 0:
        return number
    return -number

def titlelen(title):
    title=str(title)
    aa =15 -len(title)
    title = title+aa*" "
    return title

class DBCount:
    def __init__(self):
        self.conn = MySQLdb.connect(host = "localhost",\
                user="wangyu",passwd = "I@tianpin",\
                db = "pinphp_test")
        self.cur = self.conn.cursor()
        self.cur.execute("set names utf8") 
       
   
    def first_time(self):
        first_status0 = 0
        first_status1 = 0
        first_status2 = 0
        item_id = []
       # first_list_1 = []
        count = open(nowtime(),"w")

        dict_status_first = {}
        self.cur.execute("select id ,title from pin_album where global=1 or global=9")
        for pin_album in self.cur.fetchall():
           # print int(pin_album[0])
           # pin_album = LongtoInt(pin_album[0])
	   # print pin_album[0]
            self.cur.execute("select item_id from pin_album_item where album_id=%s",pin_album[0])
           # self.cur.execute("select item_id from pin_album_item where album_id=53")
            result1 = self.cur.fetchall()
            for pin_album_item in result1:
                item_id.append(pin_album_item[0])
           #     print pin_album_item[0]
                self.cur.execute("select status from pin_item where id = %s",pin_album_item[0])
                for status in self.cur.fetchall():
                    if status[0] == 0:
                        first_status0 = first_status0 + 1
                    elif status[0] == 1:
                        first_status1 = first_status1 + 1
                    elif status[0] == 2:
                        first_status2 = first_status1 + 1

            #print pin_album[1],first_status0,first_status1,first_status2
            count_file= pin_album[1]+","+str(first_status0)+","+str(first_status1)+","+str(first_status2)
            count.write(count_file)
            count.write("\n")

            dict_status_first[pin_album[0]] = first_status0,first_status1,first_status2
              # first_list_1[0] = fi first_status0 = 0
            first_status1 = 0
            first_status2 = 0
            first_status0 = 0
        #self.cur.close()
        #self.conn.close()
        return item_id,dict_status_first

    def end_file(self):
        endfilelist = []
        endfile = open(yestime(),"r")

        while True:

            endline = endfile.readline()
            endfilelist.append(str(endline))
            
            if not endline:
                break
        print endfilelist
        return endfilelist
    def start_file(self):
        startfilelist = []
        startfile= open(nowtime(),"r")
        while True:
            startline = startfile.readline()
            startfilelist.append(startline)
            if not startline:
                break
        print startfilelist
        return startfilelist
    def count_file(self,startlist,endlist):
        count_file = open(nowtime()+"count","w")
        day = nowtime()
        count_file.write(day)
        count_file.write("\n")
        title = "审核总数      通过审核       未通过审核       待审核              专辑id       专辑名称"
        count_file.write(title)
        count_file.write("\n")
        for a in range(len(endlist)):
            ss = str(startlist[a]).split(",")
            ee = str(endlist[a]).split(",")
            status0 = int(ee[1])-int(ss[1])
            status1 = int(ee[2])-int(ss[2])
            status2 = int(ss[3])-int(ee[3])
            print int(ss[1]),int(ss[2]),int(ss[3])
            print int(ee[1]),int(ee[2]),int(ee[3])

            auditing = positive_number(status1)+positive_number(status2) 
            fileline = titlelen(auditing)+titlelen(positive_number(status1))+titlelen(positive_number(status2))
            count_file.write(fileline)
            count_file.write("\n")

        count_file.close()

if __name__ == "__main__":
    dbcount = DBCount()
    dbcount.first_time()
   # while True:

        #time.sleep(1*60*60*11)
        
    #dbcount.first_time()
    end = dbcount.end_file()
    start = dbcount.start_file()
    dbcount.count_file(startlist=start,endlist=end)

    #tablename = dbcount.sqlite3_table()




