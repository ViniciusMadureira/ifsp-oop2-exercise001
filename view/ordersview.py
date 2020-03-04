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
sys.path.insert(0, "controller")
sys.path.insert(0, "model")
from itemsview import ItemsView
from itemstore import ItemStore
from order import Order
from orderstore import OrderStore
format_currency = __import__("order").Order.format_currency
clear_console = __import__("order").Order.clear_console

"""
OrdersView: View for add and list Order type objects.
"""
class OrdersView:
    
    def __init__(self):
        pass
    
    def add_order(self):        
        ido = OrderStore.ido
        print(" Ordem {} ".format(str(ido).zfill(6)).center(40, "#"))
        print("Para sair informe <s> e pressione <Enter>.")
        answer = ""
        while answer != "s":
            print("Adicionando item:".center(40))
            iv = ItemsView()
            if not iv.add_item() or answer == "s":
                break        
        order = Order()
        order.ido = ido
        order.items = ItemStore.items
        order.calculate_total() 
        OrderStore.add(order)      
        return True
    
    @staticmethod
    def list_orders(n: int = 0):   
        counter = 1
        print("\n" + " Orders ".center(60, "%") + "\n")        
        for order in OrderStore.orders.values():
            print(" Order {} ".format(str(1).zfill(6)).center(40, "#"))
            for i in order.items:
                for item in i.values():                    
                    value = format_currency(item.product.value, "R$", ",")
                    subtotal = format_currency(item.product.value * item.amount, "R$", ",")
                    print("ID: {}.\nProduto: {}.\nValor unitário: {}.\nQuantidade: {}.\nSubtotal: {}.\n".format(counter, item.product.name, value, item.amount, subtotal))
                    counter += 1
            total = format_currency(order.total, "R$", ",")
            print("Total: {}.\n".format(total))