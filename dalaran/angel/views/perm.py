#-*-coding:utf-8-*-
__author__ = 'iTianpin'


from flask import request, render_template, redirect, flash, g
from angel.model.user import get_allow_user
from angel.model.permission import set_perm, set_not_active_perm, \
    get_all_permission
from angel.model.permission_users import set_user_permission, del_user_perms, \
    get_user_perm_content
from angel.model.group import add_new_group,get_active_group
from angel.model.permission_group import set_group_permission,\
    get_perm_user_group
from angel.model.user_group import insert_user_group, del_user_group,\
    get_user_group_content
from angel.views.base import validate_user_login, require_perm

@validate_user_login
def permission_index():
    if request.method == "GET":
        return render_template("permission.html")


#权限系统权限参数加加入
@require_perm("add_perm")
@validate_user_login
def add_perm():
    if request.method == "GET":
        return render_template("add_perm.html", errno="")
    elif request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if (len(title) == 0) or (len(content) == 0):
            flash(u"请填写需要授权的部分")
            return redirect("/permission")

        set_perm(g.conn, title=title, content=content)
        flash(u"当前页面添加权限成功")
        return redirect("/permission")


#删除权限
@require_perm("del_perm")
@validate_user_login
def del_perm():
    if request.method == "GET":
        return render_template("del_perm.html", perms=get_all_permission(g.conn))
    elif request.method == "POST":
        perm_id = request.form["perm_id"]
        if len(perm_id) == 0:
            set_not_active_perm(g.conn,id=perm_id)
            return redirect("/permission")
        return render_template("del_perm.html", message=u"请填写需要修改的授权的部分")


#给用户设置权限
@require_perm("set_perm_to_user")
@validate_user_login
def set_perm_to_user():
    if request.method == "GET":
        return render_template("set_perm_to_user.html",
                               perms=get_all_permission(g.conn),
                               users=get_allow_user(g.conn))
    elif request.method == "POST":
        user_id = request.form["user_id"]
        permission_ids = request.form.getlist('perm_id')
        if (len(permission_ids) == 0) or (len(user_id) == 0):
            return redirect("/permission")
        for permission_id in permission_ids:
            set_user_permission(g.conn, user_id=int(user_id), perm_id=int(permission_id))
        flash(u"设置权限成功")
        return redirect("/permission")

#将权限加入组中
@require_perm("set_perm_to_group")
@validate_user_login
def set_perm_to_group():
    if request.method == "GET":
        return render_template("set_perm_to_group.html",
                               perms=get_all_permission(g.conn),
                               groups=get_active_group(g.conn))
    if request.method == "POST":
        group_id = request.form["group_id"]
        perm_ids = request.form.getlist("perm_id")
        if (len(group_id) == 0) or (len(perm_ids) == 0):
            return redirect("/permission")
        for perm_id in perm_ids:
            set_group_permission(g.conn, group_id=int(group_id),
                                 perm_id=int(perm_id))
        flash(u"权限分配到组成功")
        return redirect("/permission")

#将组分配给用户
@require_perm("set_group_to_user")
@validate_user_login
def set_group_to_user():
    if request.method == "GET":
        return render_template("set_group_to_user.html",
                               users=get_allow_user(g.conn),
                               groups=get_active_group(g.conn))
    if request.method == "POST":
        user_id = request.form["user_id"]
        group_ids = request.form.getlist("group_id")
        if (len(user_id) == 0) or (len(group_ids) == 0):
            return redirect("/permission")
        for group_id in group_ids:
            insert_user_group(g.conn,user_id=user_id,
                              group_id=group_id)
        flash(u"用户分配到组成功")
        return redirect("/permission")

#增加组
@require_perm("add_group")
@validate_user_login
def add_group():
    if request.method == "GET":
        return render_template("add_group.html")
    elif request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if (len(title) == 0) or (len(content) == 0):
            return redirect("/permission")
        if add_new_group(g.conn, title=title, content=content):
            flash(u"添加组成功")
            return redirect("/permission")
        return render_template("add_group.html")

#列出系统中所有的用户
@require_perm("del_user_perm_group")
@validate_user_login
def user_list():
    if request.method=="GET":
        return render_template("user_list.html",
                               users=get_allow_user(g.conn))


#查看用户权限，删除用户权限
@require_perm("del_user_perm_group")
@validate_user_login
def del_user_perm(user_id):
    if request.method == "GET":
        return render_template("del_user_perm_group.html",
                               groups=get_user_group_content(g.conn,user_id=user_id),
                               perms=get_user_perm_content(g.conn,user_id=user_id))
    elif request.method == "POST":
        del_groups = request.form.getlist("group_id")
        del_perms = request.form.getlist("perm_id")
        print del_perms
        print del_groups
        if (len(del_groups) == 0) or (len(del_perms) == 0):
            return redirect("/permission")
        for group_id in del_groups:
            del_user_group(g.conn,group_id=int(group_id),user_id=user_id)
        for perm_id in del_perms:
            del_user_perms(g.conn,perm_id=int(perm_id),user_id=user_id)
        flash(u"用户删除权限成功")
        return redirect("/permission")


#查看用户的所有权限，
@require_perm("check_user_perm")
@validate_user_login
def check_user_perm():
    return render_template("user_perm_list.html",
                           users=get_allow_user(g.conn))


@require_perm("check_user_perm")
@validate_user_login
def check_user_perm_group(user_id):
    group_perm_map = get_perm_user_group(g.conn, user_id=user_id)
    return render_template("user_perm_group.html",
                           group_perm_map=group_perm_map,
                           perms=get_user_perm_content(g.conn,user_id=user_id))


