from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from models import *
from datetime import timedelta
import requests
app = Flask(__name__)


app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:20001003@localhost:5432/test"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"   #filesystem允许用户对数据进行更改、插入、删除等操作
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'

app._static_folder = "./templates/static"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds = 1)

db.init_app(app)

#escape() 函数对 name 变量进行转义处理，比如把 < 转换成 &lt;

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        user = User(user_id, password)
        #add user successfully
        if user.addUser():
            return redirect(url_for('homepage', user_id=user.user_id))
        else:
            error_message="User's name have been used"
            return redirect(url_for('error', error_message = error_message))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #user didn't clik checkbox
        user = User(request.form.get('user_id'), request.form.get('password'))
        #如果成功登录
        if user.login():
            return redirect(url_for('homepage', user_id = user.user_id))
        else:
            error_message = "User dosen't exist or password doesn't match"
            return redirect(url_for('error', error_message = error_message))
    return render_template('login.html')


@app.route('/error/?<string:error_message>', methods=['GET','POST'])
def error(error_message):
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('error.html', error_message= error_message)


@app.route('/homepage/?<string:user_id>', methods = ['GET', 'POST'])
def homepage(user_id):
    if request.method == 'POST':
        user_input =  Book(request.form.get('isbn'),request.form.get('author'),
                      request.form.get('title'),request.form.get('year'))

        books =  user_input.search()
        return render_template('homepage.html', user_id = user_id, books = books)
    books=[Book("Please type above","--","--","--")]
    return render_template('homepage.html', user_id = user_id, books = books)



@app.route('/book/?<string:isbn>/?<string:user_id>', methods=['GET', 'POST'])
def bookpage(isbn, user_id):
    book = Book.query.filter_by(isbn = isbn).first()
    reviews = Review.query.filter_by(isbn = isbn).all()
    # using goodreags API to get average_rate
    res = requests.get("https://www.goodreads.com/book/review_counts.json",params={"key": "8lKPBXKVsRdsxFn9u0U0w", "isbns": isbn})

    try:
        res = res.json()
        average_rate = res['books'][0]['average_rating']
    except:
        average_rate=None

    if request.method == 'POST':
        comment = request.form.get('user_comment')
        for i in range(5):
            rate = request.form.get('inlineRadioOptions')
            if rate is not None: break
        review = Review(isbn, user_id, comment, rate)
        if review.addReview():
            reviews.append(review)
            return render_template('bookpage.html', book = book, reviews = reviews, user_id = user_id, average_rate = average_rate)
        else:
            # error_message = "You have commented on this book already!"
            return render_template('bookpage.html', book = book, reviews = reviews, user_id = user_id, error_message = error_message, average_rate = average_rate)
    return render_template('bookpage.html', book = book, reviews = reviews, user_id = user_id, average_rate = average_rate)


# * `200 OK`
# * `201 Created`
# * `400 Bad Request`
# * `403 Forbidden`
# * `404 Not Found`
# * `405 Method Not Allowed`
# * `422 Unprocessable Entity`
@app.route('/api/')
def review_api():
    isbn = request.args.get('isbn')
    book = Book.query.filter_by(isbn = isbn).first()
    if book:
        review_count = Review.query.filter_by(isbn = isbn).count()
        # 返回的是一个python decimal的类型需要在转换一次
        average_rating = Review.query.filter_by(isbn = isbn).with_entities(func.avg(Review.rate)).first()
        avg = float(average_rating[0])
    else:
        return jsonify({"error": "ISBN Not Found"}), 404

    return jsonify({
        "isbn" : book.isbn,
        "title": book.title,
        "author":book.author,
        "year":book.year,
        "review_count":review_count,
        "average_rating":avg
    }), 200

    # 006117758X

def createTable():
    with app.app_context():
        db.create_all()
