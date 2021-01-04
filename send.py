import argparse
from getpass import getpass
import hashlib
import server

parser = argparse.ArgumentParser()
parser.add_argument(
    '--username',
    action='store',
    help='specify which account to login to after this flag'
)
parser.add_argument(
    '--send-to',
    action='store',
    help='specify which account to send your message to after this flag'
)
parser.add_argument(
    '--whos-online',
    action='store_true',
    help='see which accounts are available for you to message'
)
parser.add_argument(
    '--new-user',
    action='store',
    help='create a new user to store in the database, specify new username after this flag'
)
args = parser.parse_args()


def create_user(user):
    pw1 = getpass('Input the password for the new account: ')
    pw2 = getpass('Confirm password: ')
    if pw1 == pw2:
        hashed = hashlib.sha256(pw1.encode('utf-8'))
        server.new_user(user, hashed.hexdigest())
    else:
        return 'Passwords don\'t match'


def get_message():
    return input('Input your message:\n')


def send_message(sender, recipient):
    if login(sender):
        msg = get_message()
        server.save_message(sender, recipient, msg)
    else:
        print('Login failed. The account may not exist or the password may be wrong.')


def login(username):
    # request to server to check credentials
    # returns true if login valid
    password = getpass('Input your password: ')
    hashed = hashlib.sha256(password.encode('utf-8'))
    return server.login(username, hashed.hexdigest())


def main():
    if args.whos_online:
        users = server.fetch_users()
        for user in users:
            print(user)
    elif args.new_user:
        create_user(args.new_user)
    elif args.send_to:
        if args.username is not None:
            send_message(args.username, args.send_to)


main()
