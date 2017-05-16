from tinydb import TinyDB

class DataBase(object):
    def __init__(self, db_filename):
        TinyDB.DEFAULT_TABLE = 'itemTable'
        self.db = TinyDB( db_filename )

    def add(self, name, status, user):
        self.db.insert_multiple([{"nameItem": name ,"statusItem": status, "nameUser": user}])
