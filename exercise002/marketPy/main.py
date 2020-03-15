# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
#from view.products_form import Ui_Form
from view.productsview import ProductsView
from controller.sqlite import SQLite

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pv = ProductsView()
    sys.exit(app.exec_())
    """
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

    import os
    path = os.path.dirname(os.path.abspath(__file__)) + '/controller/database/database.db'
    sqlite = SQLite(path)
    rows = sqlite.select("SELECT products.id, categories.id, products.name, products.description, products.value, categories.name as category FROM products INNER JOIN categories ON products.id_category = categories.id;")
    for row in rows:
        print(row)
    """
