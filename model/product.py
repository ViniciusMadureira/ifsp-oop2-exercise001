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
Product class: Model for Product type objects.
Each product contains a name (str), a description (str) and a value (float).
"""
class Product:

    def __init__(self, name: str = "", description: str = "", value: float = None):
        self.name = name
        self.description = description
        self.value = value

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
        
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = None
        try:
            if not isinstance(value, float):
                value = float(re.search(r"\d+(\.\d+)?", str(value).replace(",", ".").strip())[0])
            if value >= 0.0:                
                self.__value = int(value * 10**3) / 10**3               
        except:
            pass
    
    def is_valid(self):
        return self.__name != None and self.__description != None and self.__value != None