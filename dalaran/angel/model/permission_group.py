#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer,DateTime
from sqlalchemy.sql import select
from datetime import datetime

from base import metadata, conn
from angel.model.permission import permission
from angel.model.user_group import user_group
from angel.model.group import groups

permission_group = Table("permission_group", metadata,
                        Column("id", Integer, primary_key=True),
                        Column("group_id", Integer, index=True),
                        Column("permission_id", Integer, index=True),
                        Column("create_time", DateTime, default=lambda: datetime.now()))


def set_group_permission(connection,group_id, perm_id):
    perm_group = permission_group.insert().\
        values(group_id=group_id, permission_id=perm_id)
    connection.execute(perm_group)
    return True


def get_perm(connection,group_id):
    perms = select([permission_group.c.permission_id],
                   permission_group.c.group_id.in_(group_id))
    for row in connection.execute(perms):
        yield row


def get_user_group_perm(connection,user_id):
    perms = select([permission.c.title], permission.c.id.in_(
        select([permission_group.c.permission_id],
               permission_group.c.group_id.in_
               (select([user_group.c.group_id]).
               where(user_group.c.user_id == user_id)))))
    for row in connection.execute(perms):
        yield row


def get_perm_user_group(connection,user_id):
    stmt = select([
        groups.c.title,
        permission.c.title,
    ]) \
        .select_from(
            permission_group.join(user_group, onclause=user_group.c.group_id == permission_group.c.group_id)
                            .join(groups, onclause=groups.c.id == permission_group.c.group_id)
                            .join(permission, onclause=permission.c.id == permission_group.c.permission_id)
        ) \
        .where(user_group.c.user_id == user_id)
    group_perm_map = {}
    for group, perm in connection.execute(stmt):
        group_perm_map.setdefault(group, []).append(perm)
    return group_perm_map


def get_user_perm_content(connection,user_id):
    perms = select([permission.c.title], permission.c.id.in_(
        select([permission_group.c.permission_id],
               permission_group.c.group_id.in_
               (select([user_group.c.group_id]).
               where(user_group.c.user_id == user_id)))))
    for row in connection.execute(perms):
        yield row

