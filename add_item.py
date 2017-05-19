import argparse
from database import DataBase

def get_cmd_args():
    parser = argparse.ArgumentParser(description = "Get 'itemname', 'status' and 'user' from user input.")
    parser.add_argument('itemname', help='The name of the item to process.')
    parser.add_argument('status', help='The status of named item.')
    parser.add_argument('user', help='The user that is responsible for the item.')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    config = get_cmd_args()
    db = DataBase('//home/lidia/git/sis-project/db-library.json')
    db.add(config.itemname, config.status, config.user)
