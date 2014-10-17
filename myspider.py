#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: myspider.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-10-17
#Description: 

from scrapy import Spider, Item, Field

class Post(Item):
    title = Field()

class BlogSpider(Spider):
    name, start_urls = "blogspider",["http://blog.scrapinghub.com"]

    def prrse(self, response):
        return [Post(title=e.extract()) for e in response.css(" h2 a::text")]
