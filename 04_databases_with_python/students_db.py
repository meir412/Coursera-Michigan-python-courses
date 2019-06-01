'''
4th assignment in 4th course (databases) of the python for everybody specilization.
In this assignment we read data about students and courses from a json, Then we create an sqlite database
and store the data in it.
The db will consist of 3 tables - students, courses, and members (members model the many to many relationship between
students and courses.
'''

import sqlite3
import json

db_connection = sqlite3.connect('students_db.sqlite')
db_handler = db_connection.cursor()

db_handler.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file_name = 'roster_data.json'
string_data = open(file_name).read()
json_data = json.loads(string_data)

for record in json_data:

    student = record[0]
    course = record[1]
    role = record[2]

    db_handler.execute('''
    INSERT OR IGNORE INTO User (name)
    VALUES (?)''', (student, ))

    db_handler.execute('SELECT id FROM User WHERE name = ?', (student, ))
    student_id = db_handler.fetchone()[0]

    db_handler.execute('''
    INSERT OR IGNORE INTO Course (title)
    VALUES (?)''', (course, ))

    db_handler.execute('SELECT id FROM Course WHERE title = ?', (course, ))
    course_id = db_handler.fetchone()[0]

    db_handler.execute('''
    INSERT OR REPLACE INTO Member (user_id, course_id, role)
    VALUES (?, ?, ?)''', (student_id, course_id, role))


# The query requested for the autograder
db_handler.execute('''
SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
''')

# Answer for autograder
answer = db_handler.fetchone()
print(answer)

db_connection.commit()
db_connection.close()
