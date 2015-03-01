#-*-coding:utf-8-*-
__author__ = 'iTianpin'



from flask import request, render_template, redirect, flash,g
from angel.model.user import add_new_user, get_allow_user, delete_user, check_password, update_password,get_lock_user,set_lock_user_to_user,set_unlock
from angel.views.base import validate_user_login,require_perm

@require_perm("add_new_user")
@validate_user_login
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        repassword = request.form["repassword"]
        #Todo
        if password != repassword:
            flash(u"密码不匹配,添加用户失败",)
            return redirect("/permission")
        ip = request.remote_addr
        if (len(password) != 0) and (len(username) != 0):
            if "@itianpin.com" not in username:
                flash(u"必须使用甜品邮箱创建新账户，添加失败")
                return redirect("/add_user")
            add_new_user(g.conn,username=username,password=password,ip=ip)
            flash(u"添加用户成功")
            return redirect("/permission")
        flash(u"请填写完整认证资料")
        return redirect("/permission")

#
@require_perm("del_old_user")
@validate_user_login
def del_user():
    if request.method == "GET":
        return render_template("delete_user.html",users= get_allow_user(g.conn))
    elif request.method == "POST":
        user_id = request.form.get("user_id")
        if user_id is not None:
            delete_user(g.conn,user_id=user_id)
            flash(u"删除用户成功")
            return redirect("/permission")
        flash(u"请选择用户")
        return redirect("/delete_user")


#@require_perm("set_user_lock")
#@validate_user_login
def set_user_lock_or_unlock():
    if request.method == "GET":
        return render_template("user_lock.html",
                               lockers=get_lock_user(connection=g.conn),
                               users = get_allow_user(connection=g.conn))
    elif request.method == "POST":
        set_unlock_user_id = request.form.get("locker")
        set_lock_user_id = request.form.get("unlocker")
        print set_lock_user_id
        print set_unlock_user_id
        if len(str(set_unlock_user_id)) != 0 and len(str(set_lock_user_id)) != 0:
            set_lock_user_to_user(connection=g.conn,user_id=set_lock_user_id)
            set_unlock(connection=g.conn,user_id=set_unlock_user_id)
            return redirect("/permission")
        elif len(str(set_lock_user_id)) != 0:
            set_lock_user_to_user(connection=g.conn,user_id=set_lock_user_id)
            return redirect("/permission")
        elif len(str(set_unlock_user_id)) != 0:
            set_unlock(connection=g.conn,user_id=set_unlock_user_id)
            return redirect("/permission")
        flash(u"未选择用户")
        return redirect("/permission")

#Todo
# 这个功能暂时不上，到时看需求文档
# @require_perm("change_user_password")
# @validate_user_login
# def change_password():
#     if request.method == "GET":
#         return render_template("change_password.html", message="")
#     if request.method == "POST":
#         user_id = get_user_id_session()
#         old_password = request.form.get("old_password")
#         new_password = request.form.get("newpassword")
#         re_new_password = request.form.get("renewpassword")
#         if new_password != re_new_password:
#             return render_template("change_password.html",
#                                    message="new password not id repassword")
#         if check_password(g.conn,user_id=user_id,password=old_password):
#             update_password(user_id=user_id,password=new_password)
#             flash(u"修改成功")
#             return redirect("/permission")
#         else:
#             return render_template("change_password.html",
#                                    message=u"你输入的密码不正确")
#     return render_template("change_password.html", message="")
