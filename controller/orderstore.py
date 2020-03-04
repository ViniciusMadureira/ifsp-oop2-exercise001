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
from order import Order
from itemstore import ItemStore

"""
OrderStore: Controller to add and list Order type objects in static item's dictionary (OrderedDict).
"""
class OrderStore:

    ido = 1
    orders = OrderedDict()

    @staticmethod
    def add(order: Order):
        if order.is_valid():
            while OrderStore.exists(order.ido):
                OrderStore.ido += 1
            OrderStore.orders[OrderStore.ido] = order
            OrderStore.ido += 1
            ItemStore.clear()
            return True
        return False
    
    @staticmethod
    def exists(ido: int):
        return ido in OrderStore.orders.keys()