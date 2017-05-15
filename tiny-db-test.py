from tinydb import TinyDB, Query
#set the default table name
TinyDB.DEFAULT_TABLE = 'itemTable'

#NOTE: for future references
#for a single instance only, passing default_table to the TinyDB constructor
#TinyDB(storage=SomeStorage, default_table='my-default')

#Create the DB as a JSON file, open JSON file
db = TinyDB('//home/lidia/git/sis-project/db-library.json')

#NOTE: To use the in-memory storage, use:
#from tinydb.storages import MemoryStorage
#db = TinyDB(storage=MemoryStorage)

#Add new items
def addItem():
    #Make this into terminal variables? Or GUI?
    nameItem = input("Insert Name of the Item: ")
    statusItem = input("Insert the Status of the Item: ")
    nameUser = input("Insert the User name: ")

    #NOTE: TinyDB adds IDs to each entry
    db.insert_multiple([{'nameItem': nameItem , 'statusItem': statusItem, 'nameUser': nameUser}])

#Update items
def updateItem():
    userUpdate = input("What do you want to update?")
    db.update(fields, query)

addItem()
updateItem()
