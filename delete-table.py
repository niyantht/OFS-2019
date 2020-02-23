import sqlite3
con = sqlite3.connect('mydatabase.db')


con = sqlite3.connect('mydatabase.db')
cursor0bj = con.cursor()

cursor0bj.execute('DELETE  FROM employees where zipcode = 30005')

con.commit()