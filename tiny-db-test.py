from tinydb import TinyDB, Query


if __name__ == "__main__":
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






#This is the add item part of the program


#end result

#from inventoryDatabase import invenory_database
#db_filename = "test_database"

#if __name__ == "__main__":
#    db = invenory_database(db_filename)

#    for entry in db.get_entrie()
#    print entry


#abstraction layer

#use tiny db so the command line program does not know about the db

#insert list and update status

#mon is going to make a test
