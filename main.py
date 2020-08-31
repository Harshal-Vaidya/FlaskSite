from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import json
import os
import math
from flask_mail import Mail
# ------------------------------------------------this has been added after making parameters configurable
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random top secret string'  #----------flask secret key
app.config['UPLOAD_FOLDER'] = params['upload_location']
# ---------------------------------------gmail smtp

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)
# --------------------------------------
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
# ----------------------------------

db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    subtitle = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    slug = db.Column(db.String(21), nullable=False)
    img_file = db.Column(db.String(12), nullable=True)


@app.route("/")
def main():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))
    # [0: params['no_of_posts']]
    # posts = posts[]
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    # Pagination Logic
    # First
    if page == 1:
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif page == last:
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone, message=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        # ------------------------------smtp mail
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" + phone
                          )
    #     -----------------------smtp ends here
    return render_template('contact.html',params=params)


@app.route("/post/<string:post_slug>")
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html',params=params,post=post)

@app.route("/dashboard",methods=['GET','POST'])   #admin panel
def dashboard():
    if 'session_user' in session and session['session_user'] == params['admin_user']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params,posts=posts)

    if request.method == 'POST':
        username = request.form.get('user_name')
        userpass = request.form.get('user_password')
        if(username == params['admin_user'] and userpass == params['admin_password']):
            #set session variable
            session['session_user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params,posts=posts)

    return render_template('login.html', params=params)
#admin panel coding ends here

# edit page coding here
@app.route("/edit/<string:sno>",methods=['GET','POST'])
def edit(sno):
    if 'session_user' in session and session['session_user'] == params['admin_user']:
        if request.method == 'POST':
            input_title = request.form.get('input_title')
            input_subtitle = request.form.get('input_subtitle')
            input_slug = request.form.get('input_slug')
            input_content = request.form.get('input_content')
            input_imgfl = request.form.get('input_imgfl')

            if sno =='0':
                post = Posts(title=input_title, subtitle=input_subtitle,
                             content=input_content,date=datetime.now(),slug=input_slug,img_file=input_imgfl)
                db.session.add(post)
                db.session.commit()

            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = input_title
                post.subtitle = input_subtitle
                post.content = input_content
                post.slug = input_slug
                post.img_file = input_imgfl
                db.session.commit()
                return redirect('/edit/{{post.sno}}')
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params,post=post)


    # edit page coding ends here
    # file uploader starts here
@app.route("/upload",methods=['GET','POST'])
def uploader():
    if 'session_user' in session and session['session_user'] == params['admin_user']:
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded Succesfully"

# file uploader ends here
# coding for logout button
@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop('session_user')
    return redirect('/dashboard')

@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    if 'session_user' in session and session['session_user'] == params['admin_user']:
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')


app.run(debug=True)
