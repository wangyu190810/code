#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, Unicode, DateTime
from datetime import datetime
from sqlalchemy.sql import select
from angel.model.base import conn, metadata


login_log = Table("login_log", metadata,
                  Column("id", Integer, primary_key=True),
                  Column("login_ip", Unicode(255)),
                  Column("login_time", DateTime, default=lambda: datetime.now()),
                  Column("user_id", Integer),
                  Column("state", Integer),
                  Column("username",Unicode(255)))


#登录日志，记录用户登录时间和ip,以及是否登录成功
def insert_login(connection,ip, state,user_id=None, username=None):
    log = login_log.insert().values(user_id=user_id, login_ip=ip, state=state,username = username)
    connection.execute(log)
    return True


#登陆不成功5次，检测
def check_user_state(connection,username,today):
    stmt = select([login_log]).\
        where(login_log.c.username==username).\
        where(login_log.c.state==0).\
        where(login_log.c.login_time>=today)
    user_state = connection.execute(stmt).fetchall()
    if len(user_state) > 4:
        return True
    return False
