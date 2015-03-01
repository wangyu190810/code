#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, Unicode, DateTime

from sqlalchemy.sql import select, update


from datetime import datetime

from base import metadata, password_md5_salt,get_today
from login_log import insert_login,check_user_state

user = Table("user", metadata,
             Column("id", Integer, primary_key=True, index=True),
             Column("username", Unicode(255)),
             Column("password", Unicode(255)),
             Column("create_time", DateTime, default=lambda: datetime.now()),
             Column("last_login_ip", Unicode(255)),
             Column("last_login_time", DateTime, default=lambda: datetime.now()),
             Column("is_active", Integer, default=1, doc=u"1表示用户活跃，0表示用户被限制"),
             Column("create_ip", Unicode(255)),
             Column("is_superuser", Integer, default=0, doc=u"0表示用户是普通用户，1是超级用户"),
             Column("lock", Integer, default=0, doc=u"1表示正常，零表示用户被锁定"))


def user_login(connection,username, password, ip):
    password = password_md5_salt(password)
    login=select([user.c.id,user.c.username, user.c.password,
                  user.c.lock, user.c.is_active, user.c.is_superuser]).\
        where(user.c.username == username).\
        where(user.c.password == password)
    result = connection.execute(login).fetchall()
    if len(result) == 0:
        insert_login(connection,username=username, ip=ip, state=0)
        if check_user_state(connection=connection,username=username,today=get_today()):
            set_lock_log_to_user(connection=connection,username=username)
            return 0
        return 0
    elif len(result) == 1:
        lock = result[0][3]
        print lock
        if lock == 1:
            return -1

        set_last_ip_time(connection,username=username, ip=ip)
        insert_login(connection,user_id=result[0][0], ip=ip,username=username, state=1)
        user_id = result[0][0]
        return user_id


def get_allow_user(connection):
    users = select([user.c.id,user.c.username]).\
        where(user.c.lock == 0).\
        where(user.c.is_active == 1)
    for row in connection.execute(users):
        yield row

def get_lock_user(connection):
    stmt = select([user.c.id,user.c.username]).\
        where(user.c.lock==1).\
        where(user.c.is_active==1)
    for row in connection.execute(stmt):
        yield row


def add_new_user(connection,username, password, ip, is_superuser=0):
    password = password_md5_salt(password)
    add_user = user.insert().values(username=username, password=password,
                                    last_login_ip=ip,create_ip=ip,
                                    is_superuser=is_superuser)
    connection.execute(add_user)
    return True


def delete_user(connection,user_id):
    del_user = update(user).where(user.c.id == user_id).\
        values(lock=0, is_active=0)
    connection.execute(del_user)
    return True


def check_password(connection,user_id,password):
    password = password_md5_salt(password)
    check = select([user]).where(user.c.id == user_id).\
        where(user.c.password == password)
    if len(connection.execute(check).fetchall()) == 1:
        return True
    return False


def update_password(connection,user_id, password):
    password = password_md5_salt(password)
    find_pd= update(user).where(user.c.id == user_id).\
        values(password=password)
    connection.execute(find_pd)
    return True

def set_lock_log_to_user(connection,username):
    stmt = update(user).where(user.c.username==username).values(lock=1)
    connection.execute(stmt)


def set_lock_user_to_user(connection,user_id):
    stmt = update(user).where(user.c.id==user_id).values(lock=1)
    connection.execute(stmt)
    return True

def set_unlock(connection,user_id):
    stmt = update(user).where(user.c.id==user_id).values(lock=0)
    connection.execute(stmt)
    return True

def check_root(connection,user_id):
    root = select([user]).\
        where(user.c.id == user_id).\
        where(user.c.is_superuser == 1)
    if len(connection.execute(root).fetchall()) == 1:
        return True
    return False


def set_last_ip_time(connection,username,ip):
    last_ip_time = update(user).where(user.c.username == username).\
        values(last_login_ip=ip, last_login_time=datetime.now())
    connection.execute(last_ip_time)
    return True

