import sqlite3
import os.path
from datetime import datetime

DATABASE = 'database.db'
public_key = ''
private_key = ''


def build_database():
    print('Building database...')  # tells user database is being built
    conn, cur = establish_db_conn()

    cur.execute('''CREATE TABLE users (
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    last_login DATE NOT NULL
    );''')  # builds users table

    cur.execute('''CREATE TABLE messages (
    date DATE not null,
    sender TEXT not null,
    receiver TEXT not null,
    message TEXT,
    read INTEGER,
    FOREIGN KEY (sender) REFERENCES users(username)
    FOREIGN KEY (receiver) REFERENCES users(username)
    primary key(date, sender, receiver)
    );''')  # builds table for messages
    close_db(conn)
    print('... database built')


def establish_db_conn():  # function to open a connection to the database
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    return connection, cursor


def close_db(connection):  # function to clean up and close a database connection after finished
    connection.commit()
    connection.close()


def new_user(username, password):
    conn, cur = establish_db_conn()
    query = cur.execute('SELECT * FROM users WHERE username = ?;', (username,))  # query database for any accounts matching provided username
    if query.fetchone() is None:  # if no user is found (query will have type None)
        cur.execute('INSERT INTO users VALUES (?,?,?);', (username, password, datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))  # insert new user into database
        close_db(conn)  # and close connection
        print("User added to database")
    else:
        close_db(conn)  # otherwise close connection and tell user
        print("User already exists")


def fetch_users():
    conn, cur = establish_db_conn()
    query = cur.execute('SELECT username FROM users')
    names = [name[0] for name in query]
    return names


def fetch_messages(user):
    conn, cur = establish_db_conn()
    query = cur.execute('SELECT date, sender, message FROM messages WHERE receiver = ? AND read = 0;', (user,))
    messages = query.fetchall()
    cur.execute('UPDATE messages SET read = 1 WHERE receiver = ?', (user,))
    close_db(conn)
    return messages


def count_unread(user):
    conn, cur = establish_db_conn()
    unreads = cur.execute('SELECT COUNT(*) FROM messages WHERE receiver = ?', (user,)).fetchone()[0]
    close_db(conn)
    return f'You have {unreads} new unread messages.'


def get_key(user):
    conn, cur = establish_db_conn()
    query = cur.execute('SELECT public_key FROM users WHERE username = ?', (user,))
    return query.fetchone()


def login(user, given_hash):
    conn, cur = establish_db_conn()
    query = cur.execute('SELECT password FROM users WHERE username = ?', (user,))
    stored_hash = query.fetchone()[0]
    if given_hash == stored_hash:
        cur.execute('UPDATE users SET last_login = ? WHERE username = ?', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user,))
        close_db(conn)
        return True
    else:
        close_db(conn)
        return False


def save_message(sender, recipient, message):
    conn, cur = establish_db_conn()
    query_input = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), sender, recipient, message,)
    cur.execute('''INSERT INTO messages VALUES (?, ?, ?, ?, 0)''', query_input)
    close_db(conn)


def main():
    if not os.path.isfile(DATABASE):
        build_database()


main()
