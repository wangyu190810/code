#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: school.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2015-01-22
#Description: 

from angel.model.school import school
from flask import request,jsonify,g

def get_school(school_id):
    if request.method == "GET":
        if school_id == 0:
            return jsonify(school_info=school.get_school_info(g.conn))
        elif school_id != 0:
            return jsonify(school_info=school.get_school_info(g.conn,school_id))
    else:
        return jsonify(school_info="")



