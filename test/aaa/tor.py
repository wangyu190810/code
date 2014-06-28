#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: tor.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-27
#Description: 

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,world")

class StoryHandler(tornado.web.RequestHandler):
    def get(self,story_id):
        self.write("You requested story"+ story_id)

class HtmlHandler(tornado.web.RequestHandler):
    def get(self):
        items=["Item 1","Item 2","Item 3"]
        self.render("template.html",title="My title",items=items)


application=tornado.web.Application([
    (r"/",MainHandler),
    (r"/story/([0-9]+)",StoryHandler),
    (r"/template",HtmlHandler),
    ])

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


