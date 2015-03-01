#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, Unicode, DateTime
from sqlalchemy.sql import select
from datetime import datetime

from base import metadata, conn


"""每个开发项目自己配置自己的菜单系统"""

menu = Table("menu", metadata,
               Column("id", Integer, primary_key=True, index=True),
               Column("name", Unicode(255),unique=True,doc=u"当前项的名称"),
               Column("type",Integer,default=1,doc=u"1是目录，0是具体项"),
               Column("father_id",Integer,default=0,doc=u"根节点"),
               Column("menu_rank",Integer,default=-1,doc=u"当前简历的菜单层级"),
               Column("date", DateTime, default=lambda: datetime.now()),
               Column("group_id", Integer,default=-1,doc=u"组的具体id"),
               Column("url", Unicode(255),default=u"", doc=u"首显示url"),
               Column("doc", Unicode(255),nullable=True, doc=u"具体描述，描述这个是"),
               Column("seq",Integer,default=-1,doc=u"项目挂在位置"),
             )

def insert_sys(connection,sys=None):
    stmt = menu.insert().values(sys)
    connection.execute(stmt)


def add_sys(connection,name,doc):
    stmt = menu.insert().values(name=name,doc=doc)
    connection.execute(stmt)


def add_new_menu(connection,name,menu_rank,father_id,seq):
    stmt = menu.insert().values(name=name,father_id=father_id,seq=seq,menu_rank=menu_rank)
    connection.execute(stmt)

def add_new_action(connection,name,father_id,menu_rank,seq,doc):
    stmt = menu.insert().values(name=name,father_id=father_id,menu_rank=menu_rank,seq=seq,doc=doc)
    connection.execute(stmt)

def get_user_action(connection,name):
    stmt = select([menu.c.name,menu.c.father_id,menu.c.menu_rank,menu.c.seq]).where(menu.c.name==name)
    for row in connection.execute(stmt):
        yield stmt



