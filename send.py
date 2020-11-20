import argparse
# import cryptography

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
