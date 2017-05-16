#from tinydb import TinyDB, Query
#import sys
import argparse
from db import DataBase

def get_cmd_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('itemname', help='the name of the item to process')
    parser.add_argument('status', help='the name of the item to process')
    parser.add_argument('user', help='the name of the item to process')

    args = parser.parse_args()
    return args

# def init_db( db_filename = '//home/lidia/git/sis-project/db-library.json'):
#     TinyDB.DEFAULT_TABLE = 'itemTable'
#     db = TinyDB( db_filename )
#     return db

# def insert_item( db, item ):
#     db.insert_multiple([{"nameItem": config.itemname ,"statusItem": config.status, "nameUser": config.user}])

if __name__ == "__main__":
    config = get_cmd_args()
    db = DataBase('//home/lidia/git/sis-project/db-library.json')
    db.add(config.itemname, config.status, config.user)

    # insert_item( db, item )
#    update_item()
#    delete_item()

   # def add_item():
   #
   #     nameItem = sys.argv[1]
   #     statusItem = sys.argv[2]
   #     nameUser = sys.argv[3]
   #
   #     db.insert_multiple([{"nameItem": nameItem ,"statusItem": statusItem,"nameUser": nameUser}])

    #add_item()
