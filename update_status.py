from tinydb import TinyDB, Query
from tinydb.operations import delete
import sys

if __name__ == "__main__":

    TinyDB.DEFAULT_TABLE = 'itemTable'
    db = TinyDB('//home/lidia/git/sis-project/db-library.json')

    def update_status():
        Search = Query()

        #nameItem = input("Insert Name of the Item: ")
        db.update({"nameItem": nameItem},Search.nameItem == "INHOUSE")

        #statusItem = input("Insert the Status of the Item: ")
        db.update({"statusItem": statusItem},Search.statusItem == "INHOUSE")

        #nameUser = input("Insert the User name: ")
        db.update({"nameUser": nameUser},Search.nameUser == "INHOUSE")

    update_status()


#if user_input == "check-in item nameItem":
#   db.update({statusItem: INSTOCK}, Search.nameItem)
#   db.update({nameUser: INHOUSE}, Search.nameItem)

#if user_input == "check-out item nameItem"
#   db.update({statusItem: statusItem},Search.nameItem)
#   db.update({nameUser: nameUser},Search.nameItem)
