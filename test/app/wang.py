#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: wang.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-12-09
#Description: 

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

if __name__ == "__main__":
    app.run()


