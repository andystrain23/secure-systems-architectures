# secure-systems-architectures
# Message send and receive server prototype

## Prerequisites

You must have a terminal with the Python3 interpreter installed along with the following modules:
 - sqlite3
 - hashlib
 - argparse
 - getpass

In order to use the software you must either create an account or use one of the dummy accounts provided by the prototype account. Information on these commands is provided in section 2 of installation and usage.

## Installation and usage

To use the software you must call things using the Python3 interpreter and the commands may vary on your system based on how the interpreter was installed.

Firstly, all 3 .py files must be in the same directory.

Command usage is as follows (parts in [brackets] are where users should place their inputs):

1. Create users

Users must be created before they can be messaged. Two accounts must be set up before trying to send or receive a message. This must be done using the send script.

- `python3 send.py --new-user [USERNAME]`

The server will display a confirmation message that the database has successfully been built. The script will request a password and then add the account to the database to use later.

2. Displaying accounts to message

In order to display which accounts are available to message the user must type the following command:

- `python3 send.py --whos-online`

This will show the usernames of all the created accounts and the user will be able to send messages to any of them.

3. Sending a message

Users send messages using the following command:

- `python3 send.py --username [USERNAME] --send-to [RECIPIENT]`

The script will prompt login and then ask for the message you want to send.

4. Count unread

To show a count of the amount of unread messages for an account, use this command:

- `python3 read.py --show-unread --username [USERNAME]`

5. Receive a message

In order to receive messages from an account you must use the following command:

- `python3 read.py --username [USERNAME]`

The script will prompt for a password and then display all unread messages to this point which will mark them read.