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

    def __init__(self, id: int = None, name: str = "", description: str = "", value: float = None, category: Category = None, picture: str="", amount: int = None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__value = value
        self.__category = category
        self.__picture = picture
        self.__amount = amount

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = None;
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
            if description != None:
                description = str(description).strip()
                if 2 <= len(description) <= 400:
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
        if picture != None and re.search(r"^(\/\w+)*.(png|jpg|gif)$", picture, re.UNICODE) and len(picture) <= 96:
            self.__picture = picture

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = None;
        if amount >= 0 and amount <= 10000:
            self.__amount = amount

    def isValid(self):
        return self.id != None and self.__name != None and self.__value != None and self.__category != None and self.category.isValid() and self.__amount != None
