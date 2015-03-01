__author__ = 'iTianpin'
from sqlalchemy.schema import MetaData
from sqlalchemy import create_engine
from config import Config
import hashlib

from datetime import date

metadata = MetaData()

engine = create_engine(Config.db)


def conn():
    connect = engine.connect()
    return connect


def set_yield_to_list(yield_object):
    end_list = []
    for row in yield_object:
        end_list.append(row)
    return end_list


def password_md5_salt(password):
    md = hashlib.md5()
    for salt in range(len(password)):
        password += password[salt] * salt
    md.update(password)
    password = md.hexdigest()
    return password


def get_today():
    today = date.today()
    return today