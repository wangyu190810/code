#-*-coding:utf-8-*-
__author__ = 'iTianpin'

from flask import request,g
from angel.model.permission import get_permission_on_user
from angel.model.permission_users import get_user_permission
from angel.model.permission_group import get_perm
from angel.model.user_group import get_user_group
from angel.model.user import check_root

def check_user(user_id=None,action=None):
    if (user_id and action) is None:
        try:

            action = request.args.get("action")
            user_id = request.args.get("user_id")
            user_redirect = request.args.get("redirect")
            print user_id
            print "user_id"
        except:
            pass
    else:
        user_id = user_id
        action = action
        from angel.views.base import get_user_id
        a= check_root(g.conn,user_id=get_user_id())
        if a:
            return "1"

    from angel.views.base import set_yield_to_list

    perm_ids_user = get_user_permission(g.conn, user_id)
    perm_ids_user = set_yield_to_list(perm_ids_user)
    perms_user = get_permission_on_user(g.conn, perm_ids_user)
    perms_user = set_yield_to_list(perms_user)

    group_id = get_user_group(g.conn, user_id)
    group_id = set_yield_to_list(group_id)

    perm_ids_group = get_perm(g.conn,group_id)
    perm_ids_group = set_yield_to_list(perm_ids_group)

    perms_group =get_permission_on_user(g.conn,perm_ids_group)
    perms_group = set_yield_to_list(perms_group)
    #权限并集

    perms = perms_user+perms_group

    tag = False

    for perm in tuple(perms):
        if unicode(action) in unicode(perm):
            tag = True
            break
    perms = []
    if tag:

        return "1"

    return "0"
