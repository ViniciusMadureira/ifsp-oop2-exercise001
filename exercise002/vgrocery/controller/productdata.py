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
ProductStore class: Controller to add, delete and update Product type objects in static product's dictionary (OrderedDict).
"""
class ProductData:

    @staticmethod
    def add(product: Product):
        if not ProductStore.exists(product.name) and product.isValid():
            ProductStore.products[product.name] = product
            return True        
        return False

    @staticmethod
    def delete(productName: str):
        if ProductStore.exists(productName):
            ProductStore.products.pop(productName)
            return True
        return False

    @staticmethod
    def update(product: Product, productName: str):
        if ProductStore.exists(productName):
            ProductStore.products[product.name] = ProductStore.products.pop(productName)
            return True
        return False

    @staticmethod
    def exists(productName: str):
        return productName in ProductStore.products.keys()

    @staticmethod
    def loadProducts():
        sqlite = SQLite(SQLite.PATH)
        products = OrderedDict()
        try:
            result = sqlite.select("SELECT products.id, categories.id, products.name, products.description, products.value, products.picture, categories.name, products.amount as category FROM products INNER JOIN categories ON products.id_category = categories.id ORDER BY products.name;")
            if result:
                products = result
        except Error as e:
            print("SQLite Error. Message: {}.".format(str(e)))
        return products
