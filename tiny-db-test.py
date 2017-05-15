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
db = TinyDB('//home/lidia/git/sis-project/db-library.json')

#NOTE: To use the in-memory storage, use:
#from tinydb.storages import MemoryStorage
#db = TinyDB(storage=MemoryStorage)


db.insert_multiple([{'nameItem': 'PC' , 'statusItem': 2017-10-10, 'nameUser': 'lidi0168'}, {'nameItem': 'PC' , 'statusItem': 'INSTOCK', 'nameUser': 'INHOUSE'}])
