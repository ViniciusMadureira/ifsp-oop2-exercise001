#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Vinícius Madureira"
__email__ = "viniciusmadureira@outlook.com"
__status__ = "Testing"


from collections import OrderedDict
from model.category import Category
from controller.sqlite import SQLite
from sqlite3 import Error

"""
CategoryData class: Controller to add, delete and update Product type objects in static product's dictionary (OrderedDict).
"""
class CategoryData:        

    categories = OrderedDict()

    @staticmethod
    def add(category: Category):
        if not CategoryData.exists(category.name) and category.isValid():
            CategoryData.categories[category.name] = category
            return True
        return False

    @staticmethod
    def delete(categoryName: str):
        if CategoryData.exists(categoryName):
            CategoryData.categories.pop(categoryName)
            return True
        return False

    @staticmethod
    def update(category: Category, category_name: str):
        if CategoryData.exists(categoryName):
            CategoryData.products[category.name] = CategoryData.categories.pop(categoryName)
            return True
        return False

    @staticmethod
    def exists(categoryName: str):
        return categoryName in CategoryData.categories.keys()

    @staticmethod
    def loadCategories():
        sqlite = SQLite(SQLite.PATH)
        CategoryData.categories = OrderedDict()
        try:
            result = sqlite.select("SELECT categories.id, categories.name, categories.description FROM categories ORDER BY categories.name;")
            if result:
                CategoryData.categories = result
        except Error as e:
            print("SQLite Error. Message: {}.".format(str(e)))
        return CategoryData.categories
