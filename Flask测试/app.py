from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)


app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:20001003@localhost:5432/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"   #filesystem允许用户对数据进行更改、插入、删除等操作
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'

db.init_app(app)

#escape() 函数对 name 变量进行转义处理，比如把 < 转换成 &lt;

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')



@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        #check checkbox
        if request.form.get("checkbox"):
            user = User(request.form.get('user_id'), request.form.get('password'))
            #add user success
            if user.addUser():
                return redirect(url_for('homepage', user_id=user.user_id))

    return render_template('register.html')



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #user didn't clik checkbox
        if request.form.get("checkbox"):
            1+1
        user = User(request.form.get('user_id'), request.form.get('password'))
        #如果成功登录
        if user.login():
            return redirect(url_for('homepage'))
        else:
            return redirect(url_for('loginNoFound'))

    return render_template('login.html')

@app.route('/login/nofound', methods=['GET','POST'])
def loginNoFound():
    if request.method == 'POST':
        login()
    return render_template('login_nofound.html')


@app.route('/homepage/?<string:user_id>', methods = ['GET', 'POST'])
def homepage(user_id):
    if request.method == 'POST':
        book = Book(request.form.get('title'),
                    request.form.get('isbn'),
                    request.form.get('author'),
                    request.form.get('year'))
        if book.search():
            1+1
        else:
            return redirect(url_for('error_book_no_found'))
    return render_template('homepage.html')


def createTable():
    with app.app_context():
        db.create_all()
