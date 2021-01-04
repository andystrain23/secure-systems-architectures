import argparse
from getpass import getpass
import hashlib
import server

parser = argparse.ArgumentParser()
parser.add_argument('--stats', action='store_true', help='show how many unread messages you have, please also specify username. Without this flag, shows next unread message')
parser.add_argument('--username', action='store')
args = parser.parse_args()


def show_unread(username):
    if login(username):
        print(server.count_unread(username))
    else:
        print('Login unsuccessful, maybe password or username wrong')


def get_messages(username):
    if login(username):
        messages = server.fetch_messages(username)
        if messages is not None:
            for message in messages:
                print(f'''Date: {message[0]}
Sender: {message[1]}
Message: {message[2]}\n''')
    else:
        print("Login unsuccessful")


def login(username):
    # request to server to check credentials
    # returns true if login valid
    password = getpass('Input your password: ')
    hashed = hashlib.sha256(password.encode('utf-8'))
    return server.login(username, hashed.hexdigest())


def main():
    if args.username:
        if args.stats:
            show_unread(args.username)
        else:
            get_messages(args.username)
    else:
        print('Please enter a username')


main()
