
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
from os.path import abspath, exists, dirname
from pathlib import Path
import resources

"""
Product class: Model for Product type objects.
Each product contains a name (str), a description (str) and a value (float).
"""
class SQLite:    

    PATH = str(Path.home()) + "/vgrocery/database.db"

    def __init__(self, filename: str):
        self.__filename = filename
        self.__connect = None

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = None
        filename = filename.strip()
        try:            
            if (re.search(r"^\w{1,60}\.db$", filename, re.UNICODE)):
                self.__filename = filename
        except:
            print("Database file error. Path: {}.".format(filename))
    
    def connect(self):
        self.__connection = None
        if exists(self.__filename):
            try:
                self.__connection = sqlite3.connect(self.__filename)
            except sqlite3.Error as e:
                print("Database connection failed. Message: {}.".format(str(e)))

    def close(self):
        if self.__connection:
            self.__connection.cursor().close()

    def select(self, query: str):
        self.connect()        
        if self.__connection:
            cursor = self.__connection.cursor()
            cursor.execute(query.strip())
            rows = cursor.fetchall()
            self.close()
            return rows
        return False
    
    def insert(self, query: str, values: tuple):
        self.connect()
        if self.__connection:
            cursor = self.__connection.cursor()
            cursor.execute(query.strip(), values)
            self.__connection.commit()
            #rows = cursor.rowcount
            lastRowId = cursor.lastrowid
            self.close()
            return lastRowId
        return False
