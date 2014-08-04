#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: sqlaltest.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-31
#Description: 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func, or_, not_


DB_CONNECT_STRING = "mysql+mysqldb://root:@localhost/xxoo?charset=utf8"
engine = create_engine(DB_CONNECT_STRING,echo = True)
DB_Session = sessionmaker(bind = engine)
session = DB_Session()

#session.execute("create database adc")
#print session.execute("show databases").fetchall()

#session.execute("use abc")


BaseModel = declarative_base()
def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)

class User(BaseModel):
    __tablename__ = "user"
    id = Column(Integer,primary_key = True)
    name = Column(CHAR(30))
#init_db()

#user = User(name = "a")
#session.add(user)
#user = User(name = "b")
#session.add(user)
#user = User(name = "c")
#session.add(user)
#
#session.commit()

query = session.query(User)
#print query
#print query.statement
#
#for user in query:
#    print user.name
#
#print query.all()
#
#
print query.all()
print query.first().name
print query.filter(User.id==2).first().name
print query.offset(1).all()
print query.get(2).name
print query.filter('id=2').first().name


