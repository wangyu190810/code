#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, DateTime
from sqlalchemy.sql import select
from datetime import datetime

from base import metadata, conn
from angel.model.group import groups


user_group = Table("user_group", metadata,
                   Column("id",Integer, primary_key=True),
                   Column("group_id", Integer, index=True),
                   Column("user_id", Integer, index=True),
                   Column("create_time", DateTime, default=lambda: datetime.now()))


def insert_user_group(connection,group_id,user_id):
    add_user_group = user_group.insert().\
        values(group_id=group_id, user_id=user_id)
    connection.execute(add_user_group)
    return True


def get_user_group(connection,user_id):
    get_group = select([user_group.c.group_id]).\
        where(user_group.c.user_id == user_id)
    for row in connection.execute(get_group):
        yield row


def del_user_group(connection,group_id, user_id):
    del_group = user_group.delete().\
        where(user_group.c.group_id == group_id).\
        where(user_group.c.user_id == user_id)
    connection.execute(del_group)


def get_user_group_content(connection,user_id):
    group_content = select([groups.c.id, groups.c.title],
                    groups.c.id.in_(select([user_group.c.group_id]).
                    where(user_group.c.user_id == user_id)))
    for row in connection.execute(group_content):
        yield row
