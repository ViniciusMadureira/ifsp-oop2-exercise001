#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Vinícius Madureira"
__email__ = "viniciusmadureira@outlook.com"
__status__ = "Testing"

import sys
sys.path.insert(0, "model")
from collections import OrderedDict
from product import Product

"""
ProductStore: Controller add, delete and update Product type objects in static product's dictionary (OrderedDict).
"""
class ProductStore:

    products = OrderedDict()

    @staticmethod
    def add(product: Product):
        if not ProductStore.exists(product.name) and product.is_valid():
            ProductStore.products[product.name] = product
            return True        
        return False

    @staticmethod
    def delete(product_name: str):
        if ProductStore.exists(product_name):
            ProductStore.products.pop(product_name)
            return True
        return False

    @staticmethod
    def update(product: Product, product_name: str):        
        if ProductStore.exists(product_name): 
            ProductStore.products[product.name] = ProductStore.products.pop(product_name)
            return True
        return False

    @staticmethod
    def exists(product_name: str):
        return product_name in ProductStore.products.keys()