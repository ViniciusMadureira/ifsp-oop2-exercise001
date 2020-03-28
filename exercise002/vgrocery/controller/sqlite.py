
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Vinícius Madureira"
__email__ = "viniciusmadureira@outlook.com"
__status__ = "Testing"

import re
import sqlite3
from os.path import dirname, abspath, exists
import resources

"""
Product class: Model for Product type objects.
Each product contains a name (str), a description (str) and a value (float).
"""
class SQLite:    

    PATH = dirname(abspath(__file__)) + '/database/database.db'

    def __init__(self, file: str):        
        self.__file = file
        self.__connect = None

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = None
        try:
            filename = file.strip()
            if (re.search(r"^\w{1,60}\.db$", filename, re.UNICODE)):
                self.__file = file
        except:
            pass
    
    def connect(self):
        self.__connection = None
        if exists(self.__file):
            try:
                self.__connection = sqlite3.connect(self.__file)
            except sqlite3.Error as e:
                print("Database connection failed. Message: {}.".format(str(e)))

    def close(self):
        if self.__connection:
            self.__connection.close()

    def select(self, query: str):
        self.connect()        
        if self.__connection:
            cursor = self.__connection.cursor()
            cursor.execute(query.strip())
            rows = cursor.fetchall()
            self.close()
            return rows
        return False
    
    def insert(self, query: str):
        pass
