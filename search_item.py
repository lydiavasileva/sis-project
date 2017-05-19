import argparse
from database import DataBase
from tinydb import Query

if __name__ == "__main__":

    def get_cmd_args():
        parser = argparse.ArgumentParser(description = "Get 'itemname', 'status' and 'user' from user input.")
        parser.add_argument('itemname', help='The name of the item to process.')
        parser.add_argument('status', help='The status of named item.')
        parser.add_argument('user', help='The user that is responsible for the item.')

        args = parser.parse_args()
        return args

    get_cmd_args()
    config = get_cmd_args()
    db = DataBase('//home/lidia/git/sis-project/db/db-library.json')
    search = Query()
    print(search)
