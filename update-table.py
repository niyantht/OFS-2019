import sqlite3
con = sqlite3.connect('mydatabase.db')


cursor0bj = con.cursor()
cursor0bj. execute('UPDATE employees SET address = "3535 Caney Creek Lane (Home)" where id = 1')

con.commit()


