import sqlite3

db_connection = sqlite3.connect('count.sqlite')

db_handler = db_connection.cursor()

db_handler.execute('DROP TABLE IF EXISTS Counts')

db_handler.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')


text = open('mbox.txt')

for line in text:

    if (not line.startswith('From: ')):
        continue

    words = line.split()
    mail = words[1]
    mail_parts = mail.split(sep='@')
    org = mail_parts[1]
    db_handler.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    fetched_row = db_handler.fetchone()

    if fetched_row is None:
        db_handler.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))

    else:
        db_handler.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))


db_connection.commit()
db_connection.close()
