#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: work_count.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-28
#Description: 

import MySQLdb
class DBCount(self):
    def __init__(self):
        self.conn = MySQLdb.connect(host = "localhost",\
                user="root",passwd = "",\
                database = "pin_test")
        self.cur = conn.cursor()
        self.cur.execute("set names charset=utf8") 

    def first_time(self):
        first_status0 = 0
        first_status1 = 0
        first_status2 = 0
        item_id = []
        first_list_1 = []
        first_list = []
        dict_status_first = {}
        self.cur.execute("select id ,title from pin_album where global=1 or global=9")
        result = self.cur.fetchell()
        for pin_album in result:
            self.cur.execute("select album_id from pin_album_item where id =%s",pin_album[0])
            result1 = self.cur.fetchell()
            for pin_album_item in result1:
                item_id.append(pin_album_item[0])
                self.cur.execute("select status from pin_item where id = %s",pin_album_item)
                for status in self.cur.fetchell:
                    if first_status0 == 0:
                        first_status0 = first_status0 + 1
                    elif first_status1 == 1:
                        first_status1 = first_status1 + 1
                    elif first_status2 == 2:
                        first_status2 = first_status1 + 1

                print first_status0,first_status1,first_status2
              #  dict_status_first[pin_album[0]] = first_status0,first_status1,first_status2
               first_list_1 = first_status0,first_status1,first_status2
               first_list.append(first_list_1)
        return item_id,first_list

    def end_time(self,item_id):
        end_statuso = 0
        end_status1 = 0
        end_status2 = 0
        dict_status_end = {}

        today_status0 = 0
        today_status1 = 0
        today_status2 = 0
        list_today_1 = []
        list_today_2 = []
        list_1 = []
        list_2 = []
        self.cur.execute("select id ,title from pin_album where global=1 or global=9")

        result = self.cur.fetchell()
        for pin_album in result:
            self.cur.execute("select album_id from pin_album_item where id =%s",pin_album[0])
            result1 = cur.fetchell()
            for pin_album_item in result1:
                if pin_album_item in item_id:
                    self.cur.execute("select status from pin_item where id = %s",pin_album_item)
                    for end_status in self.cur.fetchell():

                        if end_statu0 == 0:
                            end_status0 = end_status0 + 1
                        elif end_status == 1:
                            end_status1 = end_status1 + 1
                        elif end_status == 2:
                            end_status2 = end_status2 + 1
                   # dict_status_end[pin_album_item] = end_status0,end_status1,end_status2
                    list_today_1 = end_status0,end_status1,end_status2
                    list_1.apped(list_today_1)
                else:
                    self.cur.execute("select status from pin_item where id = %s",pin_album_item)
                    for today_status in self.cur.fetchell():

                        if today_status == 0:
                            today_status0 = today_status0 + 1
                        elif today_status == 1:
                            today_status1 = today_status1 + 1

                        elif today_status == 2:
                            today_status2 = today_status2 + 1

                   # dict_status_today[pin_album_item] = today_status0,today_status1,today_status2
                    list_today_2 = today_status0,today_status1,today_status2
                    list_2.append(list_today_2)

    return list_1,list_2

if __name__ == "__main__":
    dbcount = DBCount()
    first_count = dbcount.first_time()
   # time.sleep(1*60*60*24)
    end_count = dbcount.end_time(first_count[0])
    for i in len(end_count):
        print first_count[1][i][0]-end_count[0][i][0] 
        print first_count[1][i][1]-end_count[0][i][1] 
        print first_count[1][i][2]-end_count[0][i][2]
    

        

