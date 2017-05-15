#This is the add item part of the program


#end result

from inventoryDatabase import invenory_database
db_filename = "test_database"

if __name__ == "__main__":
    db = invenory_database(db_filename)

    for entry in db.get_entrie()
    print entry


#abstraction layer

#use tiny db so the command line program does not know about the db

#insert list and update status

#mon is going to make a test
