from tinydb import TinyDB
from tinydb import Query
from tinydb.operations import delete

class DataBase(object):
    def __init__(self, db_filename):
        TinyDB.DEFAULT_TABLE = 'itemTable'
        self.db = TinyDB( db_filename )

    def add(self, name, status, user):
        self.db.insert_multiple([{"nameItem": name ,"statusItem": status, "nameUser": user}])

    def search(self, name, status, user):
        self.db.search(search.config.itemname == itemname)

    def update(self, name, status, user):
        self.db.update()
