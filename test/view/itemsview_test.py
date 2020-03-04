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
sys.path.insert(0, "view")
from productsview import ProductsView
from itemsview import ItemsView

if __name__ == "__main__":

    # Inserting products
    n = int(input()) 

    pv = ProductsView()

    for _ in range(n):            
        pv.add_product()

    # Listing products    
    ProductsView.list_products()

    # Deleting products
    pv.delete_product()
    pv.delete_product()

    # Listing products    
    pv.list_products()

    # Updating products
    pv.update()
    pv.update()
    pv.update()
    pv.update()
    pv.update()
    pv.update()

    # Inserting items
    n = int(input())

    iv = ItemsView()

    for _ in range(n):            
        iv.add_item()

    # Listing items
    iv.list_items()

    # Deleting items
    iv.delete_item()
    iv.delete_item()
    iv.delete_item()

    # Listing items
    iv.list_items()

    # Updating items
    #iv.update()
    #iv.update()
    #iv.update()    

    #exit(0)