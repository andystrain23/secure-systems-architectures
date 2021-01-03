import argparse
from getpass import getpass
# import cryptography
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
    help='create a new user to store in the database'
)
args = parser.parse_args()


def create_user(user):
    pw1 = getpass('Input the password for the new account: ')
    pw2 = getpass('Confirm password: ')
    key = 'a thing'
    #  TODO: generate and store key
    if pw1 == pw2:
        # TODO: hash password
        server.new_user(user, pw1, key)


def get_message():
    return input('Input your message:\n')


def send_message(sender, recipient):
    login(sender)
    msg = get_message()
    server.save_message(sender, recipient, msg)


def login(username):
    # request to server to check credentials
    # returns true if login valid
    password = getpass('Input your password: ')
    # hash the password
    return server.login(username, password)


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
    

    print(args)


main()
