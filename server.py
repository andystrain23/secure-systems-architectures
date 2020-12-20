import sqlite3
import os.path
from datetime import datetime

DATABASE = 'database.db'


def build_database():
    print('Building database...')  # tells user database is being built
    conn, cur = establish_db_conn()

    cur.execute('''CREATE TABLE users (
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    public_key TEXT NOT NULL,
    last_login DATE NOT NULL
    );''')  # builds users table

    cur.execute('''CREATE TABLE messages (
    date text not null,
    sender text not null,
    receiver text not null,
    message text,
    FOREIGN KEY (sender) REFERENCES users(username)
    FOREIGN KEY (receiver) REFERENCES users(username)
    primary key(date, sender, receiver)
    );''')  # builds table for messages
    close_db(conn)
    print('... database built')


def establish_db_conn():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    return connection, cursor


def close_db(connection):
    connection.commit()
    connection.close()


def new_user(username, password, p_key):
    conn, cur = establish_db_conn()
    query = cur.execute('SELECT * FROM users WHERE username = ?;', (username,))  # query database for any accounts matching provided username
    if query.fetchone() is None:  # if no user is found (query will have type None)
        cur.execute('INSERT INTO users VALUES (?,?,?,?);', (username, password, p_key, datetime.now()))  # insert new user into database
        close_db(conn)  # and close connection
        return "User added to database"
    else:
        close_db(conn)  # otherwise close connection and tell user
        return "User already exists"


def fetch_message():
    pass


def save_message():
    pass


def main():
    if not os.path.isfile(DATABASE):
        build_database()
    else:
        print('Database already built')


main()
