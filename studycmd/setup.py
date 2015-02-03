#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: setup.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2015-02-03
#Description: 

from setuptools import setup



setup(
        name = "Studycmd",
        version = "0.1.0dev",
        packages = ['studycmd'],
        entry_points={
            "console_scripts":"""
                studycmd = studycmd.prog:main
            """,
            },
        )

