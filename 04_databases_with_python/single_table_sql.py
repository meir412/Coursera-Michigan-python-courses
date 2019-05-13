
import sqlite3

db_connection = sqlite3.connect('ages.sqlite')

db_handler = db_connection.cursor()

db_handler.execute('DROP TABLE IF EXISTS Ages')

db_handler.execute('''
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)''')

db_handler.execute('''DELETE FROM Ages''')

data_list = [('Christopher', 38), ('Eisha', 36), ('Jameil', 38), ('Kruz', 13), ('Allegria', 35), ('Wasif', 39)]

for vector in data_list:

    db_handler.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', vector)

db_connection.commit()

db_handler.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

rows = db_handler.fetchall()

for row in rows:
    print(row[0])

