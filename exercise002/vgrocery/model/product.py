#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Vinícius Madureira"
__email__ = "viniciusmadureira@outlook.com"
__status__ = "Testing"

from model.category import Category
import re

"""
Product class: Model for Product type objects.
Each product contains a name (str), a description (str) and a value (float).
"""
class Product:

    def __init__(self, name: str = "", description: str = "", value: float = None, category: Category = None, picture: str=""):
        self.__name = name
        self.__description = description
        self.__value = value
        self.__category = category
        self.__picture = picture

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = None
        try:
            name = str(name).strip()
            if (re.search(r"^[\w]{2,}(\s[\d\w\-,;\+]+)*$", name, re.UNICODE) and len(name) <= 100):
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
            if (2 <= len(description) <= 400):
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
            if value >= 0.0 and value <= 100000.00:
                self.__value = int(value * 10**3) / 10**3               
        except:
            pass

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: Category):
        self.__category = None
        if category.isValid():
            self.__category = category

    @property
    def picture(self):
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = None
        if re.search(r"^\w{1,96}\.(png|jpg|gif)$", picture, re.UNICODE):
            self.__picture = picture

    def isValid(self):
        return self.__name != None and self.__value != None and self.__category != None
