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
from item import Item
from itemstore import ItemStore
from productsview import ProductsView
format_currency = __import__("order").Order.format_currency
clear_console = __import__("order").Order.clear_console

"""
ItemsView: View for list, add, delete and update Item type objects.
"""
class ItemsView:

    lst = []

    def __init__(self):
        pass
    
    def add_item(self):     
        ProductsView.list_products()
        item = Item()        
        print(" Item ".center(40, "#"))
        print("Para sair informe <s> e pressione <Enter>.")
        id = -1        
        while id not in range(1, len(ProductsView.lst) + 1):
            print("Informe o ID do produto a ser inserido e pressione <Enter>:")
            id = input()
            if id.isdigit():
                id = int(id)
            elif id == "s":
                return False   
        id -= 1
        item.product = ProductsView.lst[id]
        if ProductsView.validate_field(item, "amount", "Quantidade", "s"):
            if ItemStore.add(item):
                print("\n" + "Item cadastrado com sucesso!\nID: {}.\nProduto: {}.\nQuantidade: {}\n\n".format(id + 1, item.product.name, item.amount))
                return True                    
            print("\n" + "Falha ao adicionar item!".center(40, " ") + "\n")
        return False 

    def delete_item(self):        
        ItemsView.list_items()
        item = Item() 
        print(" Item ".center(40, "#"))
        print("Para sair informe <s> e pressione <Enter>.")
        id = -1        
        while id not in range(1, len(ItemsView.lst) + 1):
            print("Informe o ID do item a ser deletado e pressione <Enter>:")
            id = input()
            if id.isdigit():
                id = int(id)
            elif id == "s":
                return False   
        id -= 1
        item.product = ProductsView.lst[id]
        if ItemStore.delete(item.product.name):
            print("\n" + "Item '{}' removido com sucesso!".format(item.product.name).center(40, " ") + "\n")
        else:
            print("\n" + "Falha ao remover item!".center(40, " ") + "\n")

    @staticmethod
    def list_items():
        ItemsView.lst = []
        clear_console()
        print("\n" + " Items ".center(40, "#") + "\n")
        for id, item in enumerate(ItemStore.items.values(), start = 1):
            ItemsView.lst.append(item)
            value = format_currency(item.product.value, "R$", ",")
            subtotal = format_currency(item.product.value * item.amount, "R$", ",")
            print("ID: {}\nProduto: {}.\nValor unitário: {}.\nQuantidade: {}.\nSubtotal: {}.\n".format(id, item.product.name, value, item.amount, subtotal))