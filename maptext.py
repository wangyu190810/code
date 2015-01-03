#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: maptext.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2015-01-03
#Description: 

import urllib

from bs4 import BeautifulSoup

def get_index_url(url):

    content = urllib.urlopen(
            url
            )
    soup = BeautifulSoup(content)
    index_url = map(soup.find_all,"<a")
    return index_url
url = "http://www.itianpin.com"
print get_index_url(url)


