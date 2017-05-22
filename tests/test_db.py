import unittest
import os
from db import DataBase

import sys
sys.path.append( '..')

test_database_filename = 'testdata/test_database.json'
non_exists_database = 'thisfilenamedoesnotexist'


class test_database(unittest.TestCase):
    def test_create(self):
        os.remove(non_exists_database) # ensure it is not there
        my_db = DataBase( non_exists_database )
        os.remove(non_exists_database) # cleanup

    def test_open(self):
        my_db = DataBase( test_database_filename )
