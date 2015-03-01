#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, Unicode, DateTime
from sqlalchemy.sql import select

from datetime import datetime

from base import metadata, conn


permission = Table("permission", metadata,
                   Column("id", Integer, primary_key=True, index=True),
                   Column("title", Unicode(255)),
                   Column("create_time", DateTime, default=lambda: datetime.now()),
                   Column("is_active", Integer, default=1, doc=u"当前为冗余字段"),
                   Column("url", Unicode(255), doc=u"权限的纤细介绍"),
                   Column("create_user_id", Unicode(255)),
                   Column("project",Unicode(255))
                )


def set_perm(connection, title, url):
    auth = permission.insert().values(title=title, url=url)
    connection.execute(auth)
    return True


def set_not_active_perm(connection,perm_id):
    not_active = permission.update().\
        where(permission.c.id == perm_id).\
        values(is_active=0)
    connection.execute(not_active)
    return True


def get_all_permission(connection):
    perm = select([permission.c.id, permission.c.title]).\
        where(permission.c.is_active == 1)
    for row in connection.execute(perm):
        yield row


def get_permission_on_user(connection,perm_id):
    user_perm = select([permission.c.url], permission.c.id.in_(perm_id))
    for row in connection.execute(user_perm):
        yield row


