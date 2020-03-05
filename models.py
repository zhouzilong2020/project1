from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class User(db.Model):
    count = 0

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)

    user_id = db.Column(db.String, primary_key = True, nullable = False)
    password = db.Column(db.String, nullable = False)

    def __init__(self, user_id, password):
        #赋值user_id，user_password
        self.user_id = user_id
        self.password = password
        self.validity = 0

    def login(self):
        #判断当前用户是否存在  TODO::注意安全性检查！
        exist_user = db.session.execute(f"SELECT * .\
                                          FROM users .\
                                          WHERE user_id = {self.user_id} AND password = {self.password}")
        if exist_user != 0:
            validity = 1
            self.id = db
            print("login successfully!")
        else :
            print("does not exist such id or passworf faills to match")
        
    def addUser(self):
        is_exist = db.session.excute(f"SELECT count(*) .\
                                       FROM users .\
                                       WHERE user_id = {self.user_id}")
        if is_exist == 0:
            #increase user number by 1
            count += 1
            #set user unique id in database
            self.id = count
            print("regislation success!")
        else:
            print("user_id already exist!")
    
    def deleteUser(self):
        #user have logined 
        if validity == 1:
            db.session.execute(f"DELETE FROM users .\
                                 WHERE users.id = {self.")






class Book(db.Model):
    counter = 0
    __tablename__= "books"

    id = db.Column(db.Integer, primary_key = True)

    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)


class Review(db.Model):

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key = True)

    #与books的联系
    title = db.Column(db.String, db.ForeignKey("books.id"))
    book = relationship("Book", backref="review")

    #与users的联系
    review_author = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = relationship("User", backref="review")

    content = db.Column(db.String, nullable = False)
    rate = db.Column(db.Integer, nullable = False)
    
