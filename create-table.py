import sqlite3
con = sqlite3.connect('mydatabase.db')


con = sqlite3.connect('mydatabase.db')
cursor0bj = con.cursor()
cursor0bj. execute(
    "CREATE TABLE employees(id integer PRIMARY KEY, zipcode integer, address varchar)")
con.commit()

