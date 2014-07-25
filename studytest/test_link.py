#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: test_link.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-26
#Description: 

from selenium import webdriver
import time
browser=webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw1").send_keys("selenium")
browser.find_element_by_id("su1").click()
browser.maximize_window()



time.sleep(10)
browser.quit()

