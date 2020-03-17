# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from view.productsview import ProductsView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pv = ProductsView()
    #pv.pte_product_value.installEventFilter(self)
    sys.exit(app.exec_())
