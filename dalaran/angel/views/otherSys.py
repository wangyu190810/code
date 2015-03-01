__author__ = 'wangyu'
#-*-coding:utf-8-*-
import os
from flask import request, render_template, redirect, flash,g,url_for,json
from angel.model.user import add_new_user, get_allow_user, delete_user, check_password, update_password,get_lock_user,set_lock_user_to_user,set_unlock
from angel.views.base import validate_user_login,require_perm,get_user_id
from angel.model.permission import set_perm
from angel.model.permission_group import get_user_perm_content
from angel.model.menu import add_sys,add_new_menu,add_new_action
from angel.views.base import allowed_file
from werkzeug import secure_filename
from config import Config


def addSys():
    if request.method == "GET":
        return render_template("addSys.html")
    elif request.method == "POST":

        name = request.form.get("name")
        doc = ""
        #name,doc = map(request.form.get,"name","doc")
        print name,doc
        if name is None or doc is None:
            flash(u"添加失败")
            return redirect("/add_sys")
        add_sys(g.conn,name=name,doc=doc)
        flash(u"添加项目成功")
        return redirect("/add_sys")

def add_menu():
    if request.method == "GET":
        return render_template("add_menu.html")
    elif request.method == "POST":
        father_id,seq,name,menu_rank = map(request.form.get,("father_id","seq","name","menu_rank"))
        print father_id,seq,name,menu_rank
        add_new_menu(connection=g.conn,father_id=father_id,menu_rank=menu_rank,name=name,seq=seq)
        return redirect("/add_menu")

def add_sys_action():
    if request.method == "GET":
        return render_template("add_action.html")
    elif request.method == "POST":
        father_id,seq,action,menu_rank = map(request.form.get,("father_id","seq","action","menu_rank"))
        print father_id,seq,action
        add_new_action(g.conn,name=action,father_id=father_id,menu_rank=menu_rank,seq=seq,doc="具体权限点")
        return redirect("/add_action")


def user_permission_show():
    user_id = get_user_id()
    perms  = get_user_perm_content(connection=g.conn,user_id=user_id)
    for perm in perms:
        pass






def upload_json():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            a= file.read
            print a
            flash(str(a))
            file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            return redirect("upload")


#
#json 格式
# project项目
#{projec：name，{menu：name，{action：name，action:name}，{menu：name}，{menu：name}，}
"""
{
    "project" : "name",
    "menu1" : [[],[{"key1":"value1","key2":"value2"}]],
    "menu2" : [{"key3":"value3"}]

}


{
    "porject`": "wangyu",
    "menu": "[1,2,3,4,5,5]",
    "action": "add_user",
    "doc": "增加用户"
}



"""

def input_json():
    if request.method == "GET":
        return render_template("input_json.html")
    elif request.method == "POST":
        readJson = request.form.get("json")
        print readJson
        action = json.loads(readJson)
        # data = action["username"]
        # email = action["email"]
        #print data,email
        set_perm(g.conn,title=action["doc"],content=action["action"])
        return redirect("/input_json")
