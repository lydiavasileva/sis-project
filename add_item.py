from tinydb import TinyDB, Query
import sys

if __name__ == "__main__":

    TinyDB.DEFAULT_TABLE = 'itemTable'
    db = TinyDB('//home/lidia/git/sis-project/db-library.json')

    def add_item():

        nameItem = sys.argv[1]
        statusItem = sys.argv[2]
        nameUser = sys.argv[3]

        db.insert_multiple([{'nameItem': nameItem , 'statusItem': statusItem, 'nameUser': nameUser}])

    add_item()
