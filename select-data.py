import sqlite3
con = sqlite3.connect('mydatabase.db')


con = sqlite3.connect('mydatabase.db')
cursor0bj = con.cursor()

cursor0bj.execute('SELECT * FROM employees where zipcode = 30041')
rows = cursor0bj.fetchall()

for row in rows:
    print(row)


con.commit()