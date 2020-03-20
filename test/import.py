import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    cnt = 0
    for isbn, title, author, year in reader:
        cnt+=1
        year = int(year_c)
        db.execute("INSERT INTO book (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
        {"isbn": isbn, "title": title, "author": author, "year":year})
    db.commit()
    print(f"{cnt}records import successfully")

if __name__=="__main__":
    main()
