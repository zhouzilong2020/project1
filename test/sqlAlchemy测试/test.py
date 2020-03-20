from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from flask_sqlalchemy import SQLAlchemy

engine = create_engine('postgresql://postgres:20001003@localhost:5432/test', echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine) #hasn't opened any connections yet
#ervery time to creat a new session
#usage:
#new_session = Session()
db = SQLAlchemy()

class C(Base):

    __tablename__ = 'c'
    id = db.Column(db.Integer, primary_key = True)

    #与books的联系
    title = db.Column(db.String, db.ForeignKey("b.title"))
    #反向联系
    b = relationship("B", back_populates="reviews")

    #与users的联系
    user_id = db.Column(db.Integer, db.ForeignKey("a.user_id"))
    #反向联系
    a = relationship("A", back_populates="reviews")

    comment = db.Column(db.String, nullable = False)
    rate = db.Column(db.Integer, nullable = False)

class A(Base):
    __tablename__ = 'a'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)

class B(Base):
    __tablename__ = 'b'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, primary_key = True)
    isbn = db.Column(db.String, primary_key = True)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)

Base.metadata.create_all(engine)