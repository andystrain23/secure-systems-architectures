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
args = parser.parse_args()


def create_user():
    user = input('''Creating a new user \n
    Please enter the desired username (must be unique and less than 20 chars): 
    ''')
    pw1 = getpass('Password: ')
    pw2 = getpass('Confirm password: ')
    #  generate and store key
    if pw1 == pw2:
        server.new_user(user, pw1, key)
    # also need to create and store keys


def get_message(user):
    return input('Input your message:\n')


def fetch_users():
    # request to server to find all users
    pass


def send_message(sender, recipient):
    msg = get_message()
    print(msg)
    pass


def login():
    # request to server to check credentials
    # returns true if login valid
    pass


def main():
    pass


main()
