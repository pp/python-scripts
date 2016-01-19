"""
Creates a SQLite database, creates a user table
and performs a few inserts and a SELECT query.
"""

from datetime import datetime, timezone
import sqlite3

def get_datetime():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

db = sqlite3.connect(':memory:') # Create database in RAM
cursor = db.cursor()

cursor.execute('''
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  creation_time TEXT NOT NULL
);
''')
db.commit()

username1 = 'test'
email1 = 'admin@example.com'
password1 = 'abcdef'

username2 = 'user'
email2 = 'admin@newmail.com'
password2 = '123456'

cursor.execute('''
INSERT INTO users (username, email, password, creation_time)
VALUES (?,?,?,?);
''', (username1, email1, password1, get_datetime()))

cursor.execute('''
INSERT INTO users (username, email, password, creation_time)
VALUES (?,?,?,?)
''', (username2, email2, password2, get_datetime()))

db.commit()

cursor.execute('''
SELECT username, email, password, creation_time FROM users;
''')
all_rows = cursor.fetchall()
for row in all_rows:
    print('{0} {1} {2} {3}'.format(row[0], row[1], row[2], row[3]))

db.close()
