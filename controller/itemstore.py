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
from item import Item

"""
ItemStore: Controller to add, delete and list Item type objects in static item's dictionary (OrderedDict).
"""
class ItemStore:

    items = OrderedDict()

    @staticmethod
    def add(item: Item):
        if item.is_valid():
            if not ItemStore.exists(item.product.name):
                ItemStore.items[item.product.name] = item
            else:
                ItemStore.items[item.product.name].amount += item.amount
            return True
        return False
        
    @staticmethod
    def delete(product_name: str):
        if ItemStore.exists(product_name):
            ItemStore.items.pop(product_name)
            return True
        return False

    @staticmethod
    def clear():        
        ItemStore.items = OrderedDict()

    @staticmethod
    def exists(product_name: str):
        return product_name in ItemStore.items.keys()