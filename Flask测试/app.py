from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:20001003@localhost:5432/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"   #filesystem允许用户对数据进行更改、插入、删除等操作

db.init_app(app)

#escape() 函数对 name 变量进行转义处理，比如把 < 转换成 &lt;

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

def createTable():
    with app.app_context():
        db.create_all()
