import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:20001003@localhost:5432/test")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    cnt = 0
    for isbn, title, author, year in reader:
        cnt+=1
        year = int(year)
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
        {"isbn": isbn, "title": title, "author": author, "year":year})
    db.commit()
    print(f"{cnt}records import successfully")

if __name__=="__main__":
    main()
