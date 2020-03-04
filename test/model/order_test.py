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
from product import Product
from order import Order

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

    # Inserting items on order
    order = Order()
    items = {}
    n = int(input())

    for _ in range(n):
        product_name = input()
        amount = input()           
        order.add_item(product_name, amount, products)

    # Calculating total order
    order.calculate_total()

    # Printing order details
    order.print()    

exit(0)