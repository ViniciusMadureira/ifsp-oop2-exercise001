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
from product import Product
from productstore import ProductStore
format_currency = __import__('order').Order.format_currency
clear_console = __import__('order').Order.clear_console

"""
ProductsView: View for list, add, delete and update Product type objects.
"""
class ProductsView:

    lst = []

    def __init__(self):
        pass

    @staticmethod
    def validate_field(obj, field, field_name: str, cancel_value: str):
        setattr(obj, field, "")
        while getattr(obj, field) in [None, ""]:
            print(field_name + ":")
            line = input()
            setattr(obj, field, line)
            if line == cancel_value:
                return False        
        return True
    
    def add_product(self):
        product = Product()
        print("Para sair informe <s> e pressione <Enter>.")
        print(" Produto ".center(40, "#"))
        is_valid = ProductsView.validate_field(product, "name", "Nome", "s")
        if is_valid:
            is_valid = ProductsView.validate_field(product, "description", "Descrição", "s")
            if is_valid:
                is_valid = ProductsView.validate_field(product, "value", "Valor", "s")
                if not is_valid or not product.is_valid():
                    return False
                else:                    
                    if ProductStore.add(product):
                        print("\n" + "Produto '{}' cadastrado com sucesso!".format(product.name).center(40, " ") + "\n")
                        return True                    
                    print("\n" + "O produto já está cadastrado!".center(40, " ") + "\n")
        return False

    def delete_product(self):        
        ProductsView.list_products()        
        print("Para sair informe <s> e pressione <Enter>.")
        id = -1
        while id not in range(1, len(ProductsView.lst) + 1):
            print("Informe o ID do produto a ser deletado e pressione <Enter>:")
            id = input()
            if id.isdigit():
                id = int(id)
            elif id == "s":
                return False   
        id -= 1
        # print(self.lst[id].name)
        product = self.lst[id]
        if ProductStore.delete(product.name):
            print("\n" + "Produto '{}' removido com sucesso!".format(product.name).center(40, " ") + "\n")
        else:
            print("\n" + "O produto não está cadastrado!".center(40, " ") + "\n")
    
    def validate_field_onupdate(self, obj, field, field_name: str, cancel_value: str):
        anwser = ""
        while anwser not in ["s", "S", "n", "N"]:
            print("Manter {} [s] para SIM ou [n] para NÃO:".format(field_name))
            anwser = input()
            if anwser in ["n", "N"]:
                return ProductsView.validate_field(obj, field, field_name, "s")
        return True

    def update(self):
        ProductsView.list_products()
        print("Para sair informe <s> e pressione <Enter>.")
        id = -1
        while id not in range(1, len(ProductsView.lst) + 1):
            print("Informe o ID do produto a ser atualizado e pressione <Enter>:")
            id = input()
            if id.isdigit():
                id = int(id)
            elif id == "s":
                return False   
        id -= 1        
        product = self.lst[id]        
        id += 1
        product_old_name = product.name    
        value = format_currency(product.value, "R$", ",")    
        print("ID: {}\nNome: {}.\nDescrição: {}.\nValor: {}.\n\n".format(id, product.name, product.description, value))        
        is_valid = self.validate_field_onupdate(product, "name", "Nome", "s")
        if is_valid:            
            is_valid = self.validate_field_onupdate(product, "description", "Descrição", "s")
            if is_valid:
                is_valid = self.validate_field_onupdate(product, "value", "Valor", "s")
                if not is_valid or not product.is_valid():
                    return False
                else:                    
                    if ProductStore.update(product, product_old_name):
                        new_product = ProductStore.products[product.name]
                        print("\n" + "Produto atualizado com sucesso!".center(40, " "))
                        value = format_currency(new_product.value, "R$", ",")
                        print("ID: {}\nNome: {}.\nDescrição: {}.\nValor: {}.\n\n".format(id, new_product.name, new_product.description, new_product.value))   
                        return True                    
                    print("\n" + "Falha ao atualizar o produto!".center(40, " ") + "\n")
        return False

    @staticmethod
    def list_products():
        ProductsView.lst = []
        clear_console()
        print("\n" + " Produtos ".center(40, "#") + "\n")
        for id, product in enumerate(ProductStore.products.values(), start = 1):
            ProductsView.lst.append(product)
            value = format_currency(product.value, "R$", ",")
            print("ID: {}\nNome: {}.\nDescrição: {}.\nValor: {}.\n\n".format(id, product.name, product.description, value))