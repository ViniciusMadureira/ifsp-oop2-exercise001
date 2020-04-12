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
from model.product import Product
from controller.sqlite import SQLite
from sqlite3 import Error

"""
ProductData class: Controller to add, delete and update Product type objects in static product's dictionary (OrderedDict).
"""
class ProductData:

    @staticmethod
    def add(product: Product):
        if product.isValid() and not ProductData.exists(product.name):
            sqlite = SQLite(SQLite.PATH)
            try:                
                values = (product.name, product.description, product.value, product.picture, product.amount, product.category.id)
                return sqlite.insert("INSERT INTO products(name, description, value, picture, amount, id_category) VALUES (?, ?, ?, ?, ?, ?);", values)
            except Error as e:
                print("SQLite Error. Message: {}.".format(str(e)))
        return False

    @staticmethod
    def delete(productName: str):
        if ProductData.exists(productName):
            ProductData.products.pop(productName)
            return True
        return False

    @staticmethod
    def update(product: Product, productName: str):
        if ProductData.exists(productName):
            ProductData.products[product.name] = ProductData.products.pop(productName)
            return True
        return False

    @staticmethod
    def exists(productName: str):
        sqlite = SQLite(SQLite.PATH)
        try:
            result = sqlite.select("SELECT COUNT(products.id) FROM products WHERE products.name = '{}';".format(productName))
            return True if list(result[0])[0] != 0 else False
        except Error as e:
            print("SQLite Error. Message: {}.".format(str(e)))
        return True

    @staticmethod
    def load():
        sqlite = SQLite(SQLite.PATH)
        products = OrderedDict()
        try:
            result = sqlite.select("SELECT products.id, products.name, products.description, products.value, products.picture, products.amount, categories.id, categories.name as category FROM products INNER JOIN categories ON products.id_category = categories.id ORDER BY products.name;")
            if result:
               products = result
        except Error as e:
            print("SQLite Error. Message: {}.".format(str(e)))
        return products
