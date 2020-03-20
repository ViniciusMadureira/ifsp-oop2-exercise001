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
from collections import OrderedDict
sys.path.insert(0, "view")
from orderstore import OrderStore

"""
Revenues class: Revenus for Item type objects.
"""
class Revenues:

    products_sold = OrderedDict()
    total_sold = 0.0
    average_products_values = 0.0
    
    def __init__(self):
        pass

    @staticmethod
    def generate_revenues():
        total_sold = 0.0
        for order in OrderStore.orders.values():
            total_sold += order.total
            for item in order.items:
                print(item)
                Revenues.products_sold[item[0].keys()] += item.amount