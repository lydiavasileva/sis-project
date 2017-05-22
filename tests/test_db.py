import unittest
import os
from database import DataBase

import sys
sys.path.append( '..')

test_database_filename = 'testdata/test_database.json'
temp_database = 'thisdatabasemustnotexist'

test_user = "someuser"
test_status = "somestatus"
test_name = "someitem"

class test_database_basic(unittest.TestCase):
    def test_create(self):
        try:
            os.remove(temp_database) # ensure it is not there
        except OSError:
            pass
        my_db = DataBase( temp_database )
        os.remove(temp_database) # cleanup

    def test_open(self):
        my_db = DataBase( test_database_filename )


class test_database_methods(unittest.TestCase):
    def setUp( self ):
        self.tmp_db = DataBase( temp_database )

    def test_add_item(self):
        id = self.tmp_db.add( user=test_user,
                              status=test_status,
                              name=test_name )
        entry = self.tmp_db.get( id )

        self.assertEqual(entry['nameUser'], test_user)
        self.assertEqual(entry['statusItem'], test_status)
        self.assertEqual(entry['nameItem'], test_name)
