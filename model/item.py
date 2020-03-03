#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Vinícius Madureira"
__email__ = "viniciusmadureira@outlook.com"
__status__ = "Testing"

from product import Product

"""
Product class: Model for Item type objects.
Each item consists of a product (Product) and its amount (int).
"""
class Item:
    
    def __init__(self, product: Product = None, amount: int = 0):
        self.product = product
        self.amount = amount

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        self.__product = product if isinstance(product, Product) and product.is_valid() else None

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = None
        try:
            amount = int(amount)
            if (amount > 0):
                self.__amount = amount
        except:
            pass

    def is_valid(self):
        return self.__product != None and self.__amount != None 
    