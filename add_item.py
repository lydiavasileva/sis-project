from tinydb import TinyDB, Query
import argparse

if __name__ == "__main__":
    TinyDB.DEFAULT_TABLE = 'itemTable'
    db = TinyDB('//home/lidia/git/sis-project/db-library.json')

    def addItem():

        nameItem = input("Insert Name of the Item: ")
        statusItem = input("Insert the Status of the Item: ")
        nameUser = input("Insert the User name: ")

        db.insert_multiple([{'nameItem': nameItem , 'statusItem': statusItem, 'nameUser': nameUser}])

    addItem()
