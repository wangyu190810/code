#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from flask import Flask, g
from angel.views import user, login, perm, check_perm,otherSys,school
from angel.model.base import conn, Config
from datetime import timedelta



app = Flask(__name__)
app.secret_key = Config.SUCCESS_KEY
app.permanent_session_lifetime = timedelta(minutes=60)




ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#所有的接口
app.add_url_rule("/",view_func=login.index, methods=["GET"])

app.add_url_rule("/login", view_func=login.login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=login.logout, methods=["GET"])

app.add_url_rule("/permission", view_func=perm.permission_index, methods=["GET"])

app.add_url_rule("/add_user", view_func=user.add_user, methods=["GET", "POST"])
app.add_url_rule("/delete_user", view_func=user.del_user, methods=["GET", "POST"])
#app.add_url_rule("/change_password", view_func=user.change_password, methods=["GET", "POST"])


app.add_url_rule("/add_perm", view_func=perm.add_perm, methods=["GET", "POST"])
app.add_url_rule("/del_perm", view_func=perm.del_perm, methods=["GET", "POST"])

app.add_url_rule("/set_perm_to_user", view_func=perm.set_perm_to_user, methods=["GET", "POST"])
app.add_url_rule("/set_group_to_user", view_func=perm.set_group_to_user, methods=["GET", "POST"])
app.add_url_rule("/user_list", view_func=perm.user_list, methods=["GET"])
app.add_url_rule("/del_user_perm_group/<int:user_id>", view_func=perm.del_user_perm, methods=["GET", "POST"])

app.add_url_rule("/check_user_perm", view_func=perm.check_user_perm, methods=["GET"])
app.add_url_rule("/check_user_perm_group/<int:user_id>", view_func=perm.check_user_perm_group, methods=["GET"])

app.add_url_rule("/add_group", view_func=perm.add_group, methods=["GET", "POST"])
app.add_url_rule("/set_perm_to_group", view_func=perm.set_perm_to_group, methods=["GET", "POST"])


app.add_url_rule("/add_sys",view_func=otherSys.addSys,methods=["GET","POST"])
app.add_url_rule("/upload",view_func=otherSys.upload_json,methods=["GET","POST"])
app.add_url_rule("/input_json",view_func=otherSys.input_json,methods=["GET", "POST"])
app.add_url_rule("/add_menu",view_func=otherSys.add_menu,methods=["GET","POST"])
app.add_url_rule("/add_action",view_func=otherSys.add_sys_action,methods=["GET","POST"])

app.add_url_rule("/api/action_check", view_func=check_perm.check_user, methods=["GET"])

app.add_url_rule("/set_user_lock",view_func=user.set_user_lock_or_unlock,methods=["GET","POST"])

app.add_url_rule("/get_school_info/<int:school_id>",view_func=school.get_school,methods=["GET"])




@app.before_request
def _connect_db():
    g.conn = conn()


@app.teardown_request
def _disconnect_db(exception):
    if hasattr(g, "conn"):
        g.conn.close()
