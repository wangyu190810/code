__author__ = 'iTianpin'

#from angel.model import user,group,permission,permission_group,user_group,login_log,permission_users,menu
from angel.model import school 
from sqlalchemy import create_engine

from config import Config


def main():
    engine = create_engine(Config.db, echo=True)

    tables = [
          #  user.user,
          #menu.otherSys
          #    permission_group.permission_group,
          #    permission_users.permission_user,
          #    group.groups,
          #    permission.permission,
          #    user_group.user_group,
          #    login_log.login_log
          school.school
             ]
    for t in tables:
        t.create(engine, checkfirst=True)

if __name__ == "__main__":
    main()
