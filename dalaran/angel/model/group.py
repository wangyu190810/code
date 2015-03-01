#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, Unicode, DateTime
from sqlalchemy.sql import select
from datetime import datetime

from base import metadata, conn


groups = Table("groups", metadata,
               Column("id", Integer, primary_key=True, index=True),
               Column("title", Unicode(255)),
               Column("create_time", DateTime, default=lambda: datetime.now()),
               Column("is_active", Integer, default=1),
               Column("content", Unicode(255), doc=u"权限组的明细权限"),
               Column("create_user_id", Unicode(255)))


def add_new_group(connection,title, content):
    add_user = groups.insert().values(title=title, content=content)
    connection.execute(add_user)
    return True


def get_active_group(connection):
    ac_group = select([groups.c.id,groups.c.title]).where(groups.c.is_active == 1)
    for row in connection.execute(ac_group):
        yield row






