import argparse
from getpass import getpass
# toremove: import cryptography

parser = argparse.ArgumentParser()
parser.add_argument('--username', action='store')
args = parser.parse_args()

user_input = args.username
# toremove: get password from server


def login(username):
    pw_input = getpass(
        f'Hello {username}, please input your password to continue: '
    )
    print(pw_input)  # toremove: VERY DEFINITELY NOT IN FINAL CODE!!!!!!!


login(user_input)
