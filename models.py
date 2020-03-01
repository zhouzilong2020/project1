from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)

class Book(db.Model):
    __tablename__= "book"
    isbn = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)

class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key = True)
    isbn = db.Column(db.String, db.ForeignKey("book.isbn"),nullable = False)
    content = db.Column(db.String, nullable = False)
    rate = db.Column(db.Integer, nullable = False)
    review_author = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
