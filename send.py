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
    pw1 = getpass('Password: ')
    pw2 = getpass('Confirm password: ')
    key = 'a thing'
    #  generate and store key
    if pw1 == pw2:
        server.new_user(user, pw1, key)
    # also need to create and store keys


def get_message(user):
    return input('Input your message:\n')


def send_message(sender, recipient):
    msg = get_message()
    print(msg)
    pass


def login(username):
    # request to server to check credentials
    # returns true if login valid
    password = getpass('Input your password: ')
    pass


def main():
    if args.whos_online:
        users = server.fetch_users()
        for user in users:
            print(user)
    elif args.new_user:
        create_user(args.new_user)

    print(args)


main()
