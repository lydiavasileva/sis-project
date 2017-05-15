#table- items
#idItem - nameItem - statusItem - nameUser

#Example:
#1 - PC - 10-20-1344(return date) - lidi0168
#1 - PC - INSTOCK - INHOUSE


from tinydb import TinyDB, Query
#set the default table name
TinyDB.DEFAULT_TABLE = 'itemTable'

#NOTE: for future references
#for a single instance only, passing default_table to the TinyDB constructor
#TinyDB(storage=SomeStorage, default_table='my-default')


#Create the DB as a JSON file

    #do this only if db does not exist
db = TinyDB('//home/lidia/git/sis-project/db-library.json')

#NOTE: To use the in-memory storage, use:
#from tinydb.storages import MemoryStorage
#db = TinyDB(storage=MemoryStorage)


nameItem = input("Insert Name of the Item: ")
statusItem = input("Insert the Status of the Item: ")
nameUser = input("Insert the User name: ")

db.insert_multiple([{'nameItem': nameItem , 'statusItem': statusItem, 'nameUser': nameUser}])
