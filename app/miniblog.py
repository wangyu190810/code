import os
from datetime import datetime
from math import ceil
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, session, redirect, url_for, render_template, flash

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

'''Configuration - Debug can be removed for production use'''
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'data.db'),
    SECRET_KEY='not a password',
    DEBUG=True,
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True,
    USERNAME='admin',
    PASSWORD='default',
    PER_PAGE=3
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

db = SQLAlchemy(app)

'''Data model - one (Post) to many (Comment)'''
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    time=db.Column(db.String,nullable=False)
    comments=db.relationship('Comment',backref="post",lazy="dynamic")
class Comment(db.Model):
    __tablename_='comment'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Integer,nullable=False)
    role_id = db.Column(db.Integer,db.ForeignKey("posts.id"))
'''url for each post and its guest comments'''
@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    comments = post.comments.all()
    if request.method == 'POST':
        addcomments = Comment(content=request.form['reply'], post=post)
        db.session.add(addcomments)
#        return redirect(url_for('show_entries'))
    return render_template('ff.html', post=post, comments=comments)

#'''add a post if the admin is logged in'''
@app.route('/add', methods=['GET', 'POST'])
def add_entry():
#    if not session.get('logged_in'):
#        return redirect(url_for('login'))
    if request.method == 'POST':
        post=Post(title=request.form['title'], text=request.form['test'],time="asdf")
        print request.form['title'],request.form['test']
	print post
        db.session.add(post)
	print "adsfasdfa"
        flash('New entry was successfully posted')
#        return redirect(url_for('b'))
    return render_template('a.html')

#
@app.route('/')
def index():
    post=Post.query.all()
	
    return render_template("b.html",post=post)
if __name__ == '__main__':
    app.run()
