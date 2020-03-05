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
from ordersview import OrdersView

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

    # Inserting items on order
    ov = OrdersView()
    ov.add_order()    
    ov.list_orders(0)
    
    while True:
        print(" Menu ".center(60, "#"))
        print("Produtos:\n\t1 - Adicionar\n\t2 - Remover\n\t3 - Atualizar\n\t4 - Listar\nOrdens:\n\t5 - Criar\n\t6 - Listar\n7 - Sair")
        answer = int(input())
        print(answer)
        if answer == 1:
            pv.add_product()
        elif answer == 2:
            pv.delete_product()
        elif answer == 3:
            pv.update()
        elif answer == 4:
            pv.list_products()
        elif answer == 5:
            ov.add_order()
        elif answer == 6:
            print("Informe a quantidade de vendas que deseja visualizar a partir da última:")
            answer = int(input())
            ov.list_orders(answer)
        elif answer == 7:
            break