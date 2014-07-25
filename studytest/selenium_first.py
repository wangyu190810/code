#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: selenium_first.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-17
#Description: 

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Firefox()
browser.get("http://www.bing.com")
assert "Bing" in browser.title
elem=browser.find_element_by_name("p")
elem.send_keys("seleniumhp"+Keys.RETURN)
elem.sleep(0.2)
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhp.org')]")
except NoSuchElementException:
    assert 0,"can`t find selenium"

browser.close()


