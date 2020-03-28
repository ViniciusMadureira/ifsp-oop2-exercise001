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

"""
Category class: Model for Category type objects.
Each product contains a name (str), a description (str) and a value (float).
"""
class Category:

    def __init__(self, id: int = 0, name: str = "", description: str = ""):
        self.__id = id
        self.__name = name
        self.__description = description        

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = None
        if id > 0:
            self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = None
        try:
            name = str(name).strip()            
            if (re.search(r"^[\w]{2,}(\s[\d\w\-,;\+]+)*$", name, re.UNICODE) and len(name) <= 60):                
                self.__name = name
        except:
            pass

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = None
        try:
            description = str(description).strip()
            if (2 <= len(description) <= 360):
                self.__description = description
        except:
            pass

    def isValid(self):
        return self.__id != None and self.__name != None
