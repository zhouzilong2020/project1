import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

class User:
    def __init__(self, id, user_name, password):
        self.id = id
        self.user_name = user_name
        self.password = password

    def login(self):
         db.excute(