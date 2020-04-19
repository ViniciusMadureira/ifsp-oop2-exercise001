# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from view.productsview import ProductsView
#from view.statusview import StatusView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle("Windows")
    pv = ProductsView(app)
    #sv = StatusView(pv.form, True, ":/dialog-ok_icon.png", "Objeto inserido com sucesso!")
    #pv.pte_product_value.installEventFilter(self)
    sys.exit(app.exec_())
