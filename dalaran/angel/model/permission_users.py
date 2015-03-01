#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, DateTime
from sqlalchemy.sql import select
from datetime import datetime

from base import metadata, conn
from angel.model.permission import permission

permission_user = Table("permission_users", metadata,
                        Column("id", Integer, primary_key=True),
                        Column("user_id", Integer, index=True),
                        Column("permission_id", Integer, index=True),
                        Column("create_time", DateTime, default=lambda: datetime.now()))


def set_user_permission(connection,user_id, perm_id):
    perm_user = permission_user.insert().\
        values(user_id=user_id, permission_id=perm_id)
    connection.execute(perm_user)
    return True


def get_user_permission(connection,user_id):
    user_perms = select([permission_user.c.permission_id]).\
        where(permission_user.c.user_id == user_id)
    for row in connection.execute(user_perms).fetchall():
        yield row


def del_user_perms(connection,perm_id,user_id):
    del_perm = permission_user.delete().\
        where(permission_user.c.permission_id == perm_id).\
        where(permission_user.c.user_id == user_id)
    connection.execute(del_perm)
    return True


def get_user_perm_content(connection,user_id):
    perm_content = select([permission.c.id,permission.c.title,permission.c.url],permission.c.id.
                          in_(select([permission_user.c.permission_id]).
                              where(permission_user.c.user_id==user_id)))
    for row in connection.execute(perm_content):
        yield row