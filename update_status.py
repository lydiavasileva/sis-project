from tinydb import TinyDB, Query
from tinydb.operations import delete
import sys

if __name__ == "__main__":

    TinyDB.DEFAULT_TABLE = 'itemTable'
    db = TinyDB('//home/lidia/git/sis-project/db-library.json')

    def update_status():

        #nameItem = sys.argv[1]
        #statusItem = sys.argv[2]
        #nameUser = sys.argv[3]

        Status = Query()

        db.update({"nameUser": "lidi0168"},Status.nameUser == "INHOUSE")

    update_status()
