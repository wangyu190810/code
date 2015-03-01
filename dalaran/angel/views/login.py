#-*-coding:utf-8-*-
__author__ = 'iTianpin'

from flask import request, render_template, redirect, session, make_response, flash,g,Response
from angel.model.user import user_login
from angel.views.base import validate_user_login, set_sign_safe,get_user_id

from angel.model.permission_users import set_user_permission, del_user_perms, \
    get_user_perm_content
from angel.model.permission_group import set_group_permission,\
    get_perm_user_group
import time

import urllib

def login(referer=None):


    ref = request.url
    if "=" in ref:
        stat = ref.find("=")
        ref = ref[stat+1:len(ref)]
        referer = urllib.unquote(ref)


    if request.method == "GET":
        print request.form.get("referer")
        print "asdfasdf"
        return render_template("login.html",message="")

    if request.method == "POST":
        login_ip = request.remote_addr
        username = request.form["username"]
        password = request.form["password"]
        if (len(username) == 0 ) or (len(password) == 0):
            return render_template("login.html",message=u"用户名或者密码错误")
        else:
            if "@itianpin.com" not in username:
                return render_template("login.html",message=u"用户名或者密码错误")
            user_id = user_login(g.conn,username=username, password=password, ip=login_ip)
            if user_id == 0:
                return render_template("login.html",message=u"用户名或者密码错误")
            elif user_id == -1:
                flash(u"你已经被限制登陆，请找管理员！")
                return render_template("login.html",message= u"你已经被限制登陆，请找管理员！")
            if referer is not None:

                redirect_to_index = redirect(referer)
            else:

                redirect_to_index = redirect("/")
            resp = make_response(redirect_to_index)
            resp.set_cookie(key="user_id", value=set_sign_safe(str(user_id)),domain="itianpin.com",expires=time.time()+60*60)
            print request.url
            return resp


#@validate_user_login
def index():
    user_id = get_user_id()
    group_perm_map = get_perm_user_group(g.conn, user_id=user_id)
    return render_template("index.html",group_perm_map=group_perm_map,
                           perms=get_user_perm_content(g.conn,user_id=user_id))


def logout():
    resp = make_response(render_template("logout.html"))
    resp.delete_cookie(key="user_id",domain="itianpin.com")
    return resp


