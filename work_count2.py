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
def LongtoInt(value):
    assert isinstance(value,(int,long))
    return int(value & sys.maxint)

filetime = time.ctime()

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
        first_list = []
        count = open(filetime,"w")
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

            print pin_album[1],first_status0,first_status1,first_status2
            count_file= pin_album[1]+str(first_status0)+","+str(first_status1)+","+str(first_status2)
            count.write(count_file)
            count.write("\n")

            dict_status_first[pin_album[0]] = first_status0,first_status1,first_status2
              # first_list_1[0] = fi first_status0 = 0
            first_status1 = 0
            first_status2 = 0
            first_status0 = 0
              # first_list_1[1] = first_status1
              # first_list_1[2] = first_status2
              # first_list.append(first_list_1)
        #print item_id
        count.close()
        return item_id,dict_status_first
    def end_time(self,item_id):
       first_status0 = 0
       first_status1 = 0
       first_status2 = 0
       item_id = []
      # first_list_1 = []
       first_list = []
       a=0
       b=0
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
               #if list(pin_album_item[0]) in item_id:
             #  print type(pin_album_item[0])
             #  print type(item_id)
              # print type(pin_album_item[0][1])
             #  if pin_album_item[0] in item_id:

             #      a=a+1
             #  else:
             #      b=b+1
               for item_idpp in item_id:
                   print type(item_idpp[0])
                   print item_idpp[0]
                   if pin_album_item[0] == item_idpp[0]:
                       a= a +1
               print type(item_idpp[0])
               #self.cur.execute("select status from pin_item where id = %s",pin_album_item[0])
               #for status in self.cur.fetchall():
               #    if status[0] == 0:
               #        first_status0 = first_status0 + 1
               #    elif status[0] == 1:
               #        first_status1 = first_status1 + 1
               #    elif status[0] == 2:
               #        first_status2 = first_status1 + 1
           #print type(item_idpp)
           print first_status0,first_status1,first_status2
           dict_status_first[pin_album[0]] = first_status0,first_status1,first_status2
             # first_list_1[0] = fi first_status0 = 0
           first_status1 = 0
           first_status2 = 0
           first_status0 = 0
             # first_list_1[1] = first_status1
         
             # first_list_1[2] = first_status2
             # first_list.append(first_list_1)
       #print item_id
       # return item_id,dict_status_first
           print a
           print b

if __name__ == "__main__":
    dbcount = DBCount()
    dbcount.first_time()
#    first_count = dbcount.first_time()

   # time.sleep(1*60*60*24)
    #end_count = dbcount.end_time(first_count[0])
   # for i in len(end_count):
   #     print first_count[1][i][0]-end_count[0][i][0] 
   #     print first_count[1][i][1]-end_count[0][i][1] 
   #     print first_count[1][i][2]-end_count[0][i][2]
   # 
    #dbcount.day_time(first_count[0])
 #   dbcount.end_time(first_count[1])

        

