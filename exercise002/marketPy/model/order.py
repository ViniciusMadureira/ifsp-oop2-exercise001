#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Vinícius Madureira"
__copyright__ = "Copyright 2020, Vinícius Madureira"
__license__ = "Creative Commons Zero 1.0 Universal"
__version__ = "0.01a"
__maintainer__ = "Vinícius Madureira"
__email__ = "viniciusmadureira@outlook.com"
__status__ = "Testing"

import os

"""
Order class: Model for Order type objects.
Each order consists of a list of items (list(Item)), which are not repeated. Each item has a product (Product) - which has a name (str) and a value (float), and its amount (float). As the final attribute of the order, the total value (float) is calculated after all items are inserted.
"""
class Order:

    def __init__(self):
        self.__ido = None
        self.__items = []
        self.__total = 0

    @property
    def ido(self):
        return self.__ido

    @ido.setter
    def ido(self, ido: int):        
        if ido > 0:
            self.__ido = ido

    @property
    def total(self):
        return self.__total
    
    def calculate_total(self):        
        for i in self.__items:
            for item in i.values():
                self.__total += item.product.value * item.amount

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        if len(items) > 0:
            self.__items.append(items)

    @staticmethod
    def clear_console():
        try:
            # Clear console on Windows Systems
            clear = lambda: os.system("cls")
            clear()
        except:
            try:
                # Clear console on Unix Systems
                clear = lambda: os.system("clear")
                clear()
                clear = lambda: os.system("reset")
                clear()
            except:
                pass

    @staticmethod
    def format_currency(value, symbol, decimal_separator):
        return symbol + f"{value:.2f}".replace(".", decimal_separator)

    def print(self):
        Order.clear_console()        
        for item in self.__items[0].values():
            sub_total = Order.format_currency(item.product.value * item.amount, "R$", ",")
            value = Order.format_currency(item.product.value, "R$", ",")
            print("Item: {}.\nQuantidade: {}.\nValor unitário: {}.\nSubtotal: {}.\n".format(item.product.name, item.amount, value, sub_total))
        total = Order.format_currency(self.__total, "R$", ",")        
        print("Valor final: {}.".format(total))

    def is_valid(self):
        return len(self.__items) > 0