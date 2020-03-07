from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class User(db.Model):
    count = 0

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)

    user_id = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)

    def __init__(self, user_id, password):
        #赋值user_id，user_password
        self.user_id = user_id
        self.password = password
        self.validity = 0

    def currentStatus(self):
        return True if validity == 1 else False
        

    #log in user
    def logIn(self):
        #判断当前用户是否存在  TODO::注意安全性检查！
        exist_user_password = db.session.execute(f"SELECT password .\
                                          FROM users .\
                                          WHERE user_id = {self.user_id}").first()
        #当前用户名存在，并且密码匹配
        if exist_user_password is not None: 
            if exist_user_password == self.password:
                validity = 1
                print("login successfully!")
        else:
            print("does not exist such id or passworf faills to match")

    #log out user
    def logOut(self):
        if validity == 1:
            validity = 0
            print("you have logged out")
        else:
            print("error!")
        
    #add a new user
    def addUser(self):
        is_exist = db.session.excute(f"SELECT count(*) .\
                                       FROM users .\
                                       WHERE user_id = {self.user_id}")
        #current user_id does not exist
        if is_exist == 0:
            #increase user number by 1
            count += 1
            #set user unique id in database
            self.id = count
            print("regislation success!")
        else:
            print("user_id already exist!")

    #delete an user
    def deleteUser(self):
        #user have validity
        if validity == 1:
            db.session.execute(f"DELETE FROM users .\
                                 WHERE users.id = {self.user_id}")
            print("current user have been removed")
        else:
            print("please log in first")


class Book(db.Model):
    counter = 0
    __tablename__= "books"

    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String, primary_key = True, unique = True)
    isbn = db.Column(db.String, primary_key = True)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)

    def __init__(self, isbn, auther, title):
        self.isbn = isbn
        self.auther = auther
        self.title = title

    #insert a book to database
    def insert(self):
        count+=1
        self.id = Book.id
        db.session.excute("") #TODO

    #search a book through isbn/auther/title with partialy or entirely information 
    def search(self):
        isbnExist = db.session.excute(f"SELECT * .\
                                        FROM books .\
                                        WHERE books.isbn LIKE ''%{self.isbn}%'' ").fetchall()
        titleExist = db.session.excute(f"SELECT * .\
                                         FROM books .\
                                         WHERE books.title LIKE ''%{self.title}%'' ").fetchall()
        AuthorExist = db.session.excute(f"SELECT * .\
                                          FROM books .\
                                          WHERE books.title LIKE ''%{self.author}%'' ").fetchall()
        return [isbnExist, titleExist, AuthorExist]


class Review(db.Model):
    count = 0

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key = True)

    #TODO: read reference paper！https://docs.sqlalchemy.org/en/13/core/constraints.html
    #与books的联系
    title = db.Column(db.String, db.ForeignKey("books.title"), nullable = False)
    #反向联系
    book = relationship("Book", back_populates="reviews")

    #与users的联系
    user_id = db.Column(db.String, db.ForeignKey("users.user_id"), nullable = False)
    #反向联系
    users = relationship("User", back_populates="reviews")

    comment = db.Column(db.String, nullable = False)
    rate = db.Column(db.Integer, nullable = False)
    
    def writeReview(self, comment, title, rate, revier_author):
        count +=1
        self.id = Review.id
        db.session.excute(f"INSERT INTO reviews .\
                           (id, title, user_id, comment, rate) .\
                           VALUES ('{self.id}','{self.title}', '{self.user_id}', '{self.comment}', '{self.rate}' ")
        print("comment success!")
        



        