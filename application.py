import os
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

#local database:: postgresql://postgres:20001003@localhost:5432/test
# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgresql://postgres:20001003@localhost:5432/test")
db = scoped_session(sessionmaker(bind=engine)) #db is a session and is bind to engine


#key: 8lKPBXKVsRdsxFn9u0U0w
#secret: fkwQ0OK4E80EiOmiwWnGcsAv1S3F4ylOVn0MHjlM

@app.route("/")
def index():
    return "Project 1: TODO"

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
