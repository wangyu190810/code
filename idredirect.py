#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: redirect.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-08-12
#Description: 

import urllib2
from bs4 import BeautifulSoup
from xml.sax.saxutils import unescape
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from random import randint
#from pyvirtualdisplay import Display

def filetreat():
    urllist = []
    urllistend = []
    urldict = {}
    i = 0
    with open("330redirect.txt") as e:
        while True:
  
            fileline = e.readline()
            if not fileline:

                break  
            i = i +1
            start = len(fileline)
            start = fileline.find("http")
            end = fileline.find("p=mm_")
            url = fileline[start:end+30]
            urlid = fileline[end+30:end+36]
            print url
            print ""
            a = urlid.strip()
            print a
            urllist = [a,url]
            urllistend.append(urllist)

    return urllistend

def urlid(driver,p):
    soup = BeautifulSoup(p)
    Trueurl = soup.find_all("a",class_="featured-btn go-to-buy")
    if Trueurl:
        juckdata = str(Trueurl)[41:-32]
        urlstart = juckdata.replace("&amp;","&")
        print urlstart
        #ff.write(urlstart)
        driver.get(urlstart)
        idurl = driver.current_url
        return idurl

def urltreat():
    bugurl = []
    sleeptime = 0
    chromedriver = "/home/wang/Desktop/chromedriver"
    os.environ["webdriver.chrome.webdriver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

   # driver = webdriver.Firefox()
    ff = open("330urltimeoutid.txt","a")
    urllistend = filetreat()
    #print urldict[0]
    #print urldict[1]
    #print urldict[2]
    for key,value in urllistend:
        
        print key,value

        print type(key),type(value)
        print key,value
        try:
            f = urllib2.urlopen(
                    url = value
                    )
            p = f.read()
            idurl = urlid(driver,p) 
        
      
            ff.write(idurl)
            ff.write("     "+key)
            ff.write("\n")
            ff.flush()
        except TypeError:
            print "ads"
        except ValueError:
            print "asdf"


    ff.close()
    driver.close()

if __name__ == "__main__":
    urltreat()

