#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, Unicode, DateTime,Float
from sqlalchemy.sql import select

from datetime import datetime

from base import metadata, conn


school = Table("school", metadata,
                Column("id", Integer, primary_key=True, index=True),
                Column("name", Unicode(255)),
                Column("chiname", Unicode(255)),
                Column("schoollogo", Unicode(255), doc=u"学校图标"),
                Column("official", Unicode(255), doc=u"学校的官网地址"),
                Column("baidu", Unicode(255), doc=u"百度介绍"),
                Column("wiki", Unicode(255), doc=u"wiki介绍"),
                Column("menaGPA", Unicode(255), doc=u""),
                Column("latitude", Float, doc=u"经度"),
                Column("longitude", Float,doc=u"纬度"),
                Column("country",Unicode(255)),
                Column("city",Unicode(255))
                )


def get_school_info(connection,school_id=None):
    if school_id is None:
        stmt = select([school])
        return connection.execute(stmt)
    else:
        stmt = select([school]).where(school.c.id == school_id)
        return connection.execute(stmt)

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


