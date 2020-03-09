from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug import generate_password_hash, check_password_hash
db = SQLAlchemy()


class User(db.Model):
    count = 0

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)

    user_id = db.Column(db.String, primary_key = True, unique = True)
    #hash value of password
    password_hash = db.Column(db.String, nullable = False)
    password = None

    #password is transfered into hash value
    def __init__(self, user_id, password):
        #赋值user_id，user_password
        self.user_id = str(user_id)
        self.password = str(password)
        self.validity = 0
    
    def __repr__(self):
        return '<user %s>' % self.user_id

    def currentStatus(self):
        return True if validity == 1 else False

    def set_password(self):
         #save password hash value into class's attribute
         self.password_hash = generate_password_hash(self.password)

    def validate_password(self, password):
        #return a boolen value
        return check_password_hash(self.password_hash, password)

    #log in user
    def login(self):
        #判断当前用户是否存在
        try:
            exist_user_password = db.session.execute(f'''SELECT password \
                                                         FROM users \
                                                         WHERE user_id == "{self.user_id}" ''').first()
            #当前用户名存在，并且密码匹配
            if exist_user_password is not None:
                if validate_password(exist_user_password):
                    validaty = 1
            return True
        except:
            return False

    #log out user
    def logout(self):
        if validity == 1:
            validity = 0
            print("you have logged out")
        else:
            print("error!")

    #add a new user
    def addUser(self):
        is_exist = db.session.execute(f"SELECT * \
                                       FROM users \
                                       WHERE user_id = '{self.user_id}' ").first()
        #current user_id does not exist
        if is_exist is None:
            #increase user number by 1
            User.count += 1
            #set user unique id in database
            self.id = User.count
            self.set_password()
            db.session.execute(f"INSERT INTO users\
                                 (id, user_id, password_hash)\
                                 VALUES('{self.id}', ‘{self.user_id}', '{self.password_hash}')")
            return True
        else:
            return False

    #delete an user
    def deleteUser(self):
        #user have validity
        if validity == 1:
            db.session.execute(f"DELETE FROM users .\
                                 WHERE users.id = '{self.user_id}'")
            print("current user have been removed")
        else:
            print("please log in first")


class Book(db.Model):
    counter = 0
    __tablename__= "books"

    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String)
    isbn = db.Column(db.String, unique = True)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)

    def __init__(self, isbn, auther, title, year):
        self.isbn = isbn
        self.auther = auther
        self.title = title
        self.year = year

    #insert a book to database
    def insert(self):
        count+=1
        self.id = Book.id
        db.session.excute("") #TODO

    #search a book through isbn/auther/title with partialy or entirely information
    def search(self):
        try:
            isbnExist = db.session.excute(f"SELECT * \
                                            FROM books \
                                            WHERE books.isbn LIKE ''%{self.isbn}%'' ").fetchall()
            titleExist = db.session.excute(f"SELECT * \
                                             FROM books \
                                             WHERE books.title LIKE ''%{self.title}%'' ").fetchall()
            AuthorExist = db.session.excute(f"SELECT * \
                                              FROM books \
                                              WHERE books.title LIKE ''%{self.author}%'' ").fetchall()
            return [isbnExist, titleExist, AuthorExist]
        except:
            return False


class Review(db.Model):
    count = 0

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key = True)

    #TODO: read reference paper！https://docs.sqlalchemy.org/en/13/core/constraints.html
    #与books的联系
    isbn = db.Column(db.String, db.ForeignKey("books.isbn"), nullable = False)
    #反向联系
    book = relationship("Book", backref=db.backref('reviews', lazy='dynamic'))

    #与users的联系
    user_id = db.Column(db.String, db.ForeignKey("users.user_id"), nullable = False)
    #反向联系
    users = relationship("User", backref=db.backref('reviews', lazy='dynamic'))

    comment = db.Column(db.String, nullable = False)
    rate = db.Column(db.Integer, nullable = False)

    def writeReview(self, comment, title, rate, revier_author):
        count +=1
        self.id = Review.id
        db.session.excute(f"INSERT INTO reviews .\
                           (id, title, user_id, comment, rate) .\
                           VALUES ('{self.id}','{self.title}', '{self.user_id}', '{self.comment}', '{self.rate}' ")
        print("comment success!")
