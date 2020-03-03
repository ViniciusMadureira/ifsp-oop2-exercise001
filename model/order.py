#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Vinícius Madureira"
__email__ = "viniciusmadureira@outlook.com"
__status__ = "Testing"

from item import Item
import os

"""
Product class: Model for Order type objects.
Each order consists of a list of items (list(Item)), which are not repeated. Each item has a product (Product) - which has a name (str) and a value (float), and its amount (float). As the final attribute of the order, the total value (float) is calculated after all items are inserted.
"""
class Order:

    def __init__(self):
        self.__items = {}
        self.__total = 0
        pass

    @property
    def total(self):
        return self.__total
    
    def calculate_total(self):
        for item in self.__items.values():
            self.__total += item.product.value * item.amount

    @property
    def items(self):
        return self.__items

    def add_item(self, product_name: str, amount: int, products: dict):
        if product_name in products.keys():
            item = Item()
            item.product = products[product_name]
            item.amount = amount
            if item.is_valid():
                if item.product.name not in self.__items.keys():
                    self.__items[item.product.name] = item
                else:
                    self.__items[item.product.name].amount += item.amount

    def clear_console(self):
        try:
            # Clear console on Windows Systems
            clear = lambda: os.system("cls")
            clear()
        except:
            try:
                # Clear console on Unix Systems
                clear = lambda: os.system("clear")
            except:
                pass
    
    def print(self):
        self.clear_console()
        for item in self.__items.values():
            sub_total = item.product.value * item.amount
            print("Item: {}.\nQuantidade: {}.\nValor unitário: R${:.2f}.\nValor total: R${:.2f}.\n".format(item.product.name, item.amount, item.product.value, sub_total))            
        print("Valor final: R${:.2f}.".format(self.__total))   

    def is_valid(self):
        return len(self.__items > 0)  