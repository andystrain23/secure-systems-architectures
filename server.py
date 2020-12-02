import sqlite3
import os.path
import time

DATABASE = 'database.db'


def build_database():
    print('Building database...')
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()

    c.execute('''CREATE TABLE users (
    username TEXT UNIQUE,
    password TEXT,
    last_login DATE
    )''')

    c.execute('''CREATE TABLE messages (
    date DATE NOT NULL,
    sender TEXT NOT NULL,
    receiver TEXT NOT NULL,
    message TEXT,
    FOREIGN KEY (sender) REFERENCES users(username)
    FOREIGN KEY (receiver) REFERENCES users(username)
    PRIMARY KEY (date, sender, receiver)
    )''')
    connection.commit()
    connection.close()
    time.sleep(1)
    print('... database built')


if not os.path.isfile(DATABASE):
    build_database()
else:
    print('Database already built')
