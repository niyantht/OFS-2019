

import sqlite3
con = sqlite3.connect('mydatabase.db')

entities = (3, 30005, '420 Prospect Place')
con = sqlite3.connect('mydatabase.db')
cursor0bj = con.cursor()
cursor0bj. execute(
    'INSERT INTO employees(id, zipcode, address) VALUES (?, ?, ?)', entities)



con.commit()


