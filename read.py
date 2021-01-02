import argparse
from getpass import getpass
# toremove: import cryptography
import server

parser = argparse.ArgumentParser()
parser.add_argument('--username', action='store')
args = parser.parse_args()

username = args.username
# toremove: get password from server


def login(user):
    pw_input = getpass(
        f'Hello {user}, please input your password to continue: '
    )
    pw_confirm = getpass('Please confirm your password: ')
    if pw_input == pw_confirm:
        pass
    else:
        print('Passwords didn\'t match, please try again.')


login(username)
