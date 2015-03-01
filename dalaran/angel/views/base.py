#! -*-coding:utf-8-*-
__author__ = 'iTianpin'

from flask import render_template, redirect, flash,request
from functools import wraps
from itsdangerous import Signer
from config import Config


from check_perm import check_user


def validate_user_login(func):
    @wraps(func)
    def _validate_user_login(*args, **kwargs):
        if  request.cookies.get("user_id") is None:
            return redirect("/login")
        elif request.cookies.get("user_id") is not None:
            try:
                get_sign_safe(request.cookies.get("user_id"))
                return func(*args, **kwargs)
            except:
                return redirect("/login")
    return _validate_user_login


def require_perm(perm):
    def validate_user_login(func):
        @wraps(func)
        def _validate_user_login(*args,**kwargs):
            if request.cookies.get("user_id") is None:
                return redirect("/login")
            elif request.cookies.get("user_id") is not None:
                user_id = get_sign_safe(request.cookies.get("user_id"))
                result = check_user(user_id, perm)
                if result == "0":
                    flash(u"你没有 %s 的权限" % perm)
                    return redirect("/permission")
                return func(*args,**kwargs)
        return _validate_user_login
    return validate_user_login




def set_yield_to_list(yield_object):
    end_list = []
    for row in yield_object:
        row = list(row)[0]
        end_list.append(row)
    return end_list


@validate_user_login
def success():
    return render_template("success.html")


def get_user_id():
    user_id = get_sign_safe(request.cookies.get("user_id"))
    return user_id

def set_sign_safe(sign_file):
    s = Signer(Config.login_sign)
    return s.sign(sign_file)


def get_sign_safe(true_file):
    s= Signer(Config.login_sign)
    return s.unsign(true_file)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
