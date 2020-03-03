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
sys.path.insert(0, "../model")
from product import Product
from item import Item

if __name__ == "__main__":

# Inserting products    
    products = {}
    n = int(input())
    
    for _ in range(n):
        product = Product()
        product.name = input()
        product.description = input()
        product.value = input()
        products[product.name] = product
        
    for product in products.values():
        if not product.is_valid():
            exit(1)

# Inserting items
    items = {}
    n = int(input())

    for _ in range(n):
        product_name = input()
        amount = input()           
        if product_name in products.keys():                          
            item = Item()
            item.product = products[product_name]
            item.amount = amount
            if item.is_valid():
                if item.product.name not in items.keys():
                    items[item.product.name] = item
                else:
                    items[item.product.name].amount += item.amount    
    
    for item in items.values():        
        print("Item: {}.\nQuantidade: {}.\nValor unitário: R${:.2f}.\nValor total: R${:.2f}.\n".format(item.product.name, item.amount, item.product.value, item.product.value * item.amount))
    
    exit(0)