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

def registerFun():
    if not request.form.get("checkbox"):
        error_message = "Pleas check the user's aggreement first!"
        return redirect(url_for('registerError', error_message = error_message))

    user_id = request.form.get('user_id')
    password = request.form.get('password')
    # empty input
    if user_id == '' or password == '':
        error_message = "User's id and password cann't be empty!"
        return redirect(url_for('registerError', error_message = error_message))

    user = User(user_id, password)
    #add user successfully
    if user.addUser():
        return redirect(url_for('homepage', user_id=user.user_id))
    else:
        error_message="Opps someting just happened, please try again or contact administrator"
        return redirect(url_for('registerError', error_message = error_message))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        registerFun()
    return render_template('register.html')


@app.route('/register/error/?<string:error_message>', methods=['GET','POST'])
def registerError(error_message):
    if request.method == 'POST':
        registerFun()
    return render_template('register_error.html', error_message= error_message)





@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #user didn't clik checkbox
        user = User(request.form.get('user_id'), request.form.get('password'))
        #如果成功登录
        if user.login():
            return redirect(url_for('homepage'))
        else:
            error_message = "User dosen't exist or password doesn't match"
            return redirect(url_for('loginError', error_message = error_message))

    return render_template('login.html')

@app.route('/login/error/?<string:error_message>', methods=['GET','POST'])
def loginError(error_message):
    if request.method == 'POST':
        login()
    return render_template('login_error.html', error_message= error_message)


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
    return render_template('homepage.html', user_id = user_id)


def createTable():
    with app.app_context():
        db.create_all()
