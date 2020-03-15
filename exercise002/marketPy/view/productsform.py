# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productsform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(980, 580)
        Form.setMinimumSize(QtCore.QSize(980, 580))
        Form.setMaximumSize(QtCore.QSize(980, 580))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.pte_product_name = QtWidgets.QPlainTextEdit(Form)
        self.pte_product_name.setGeometry(QtCore.QRect(610, 90, 351, 41))
        self.pte_product_name.setObjectName("pte_product_name")
        self.hline1 = QtWidgets.QFrame(Form)
        self.hline1.setGeometry(QtCore.QRect(0, 450, 991, 20))
        self.hline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline1.setObjectName("hline1")
        self.lbl_product_description = QtWidgets.QLabel(Form)
        self.lbl_product_description.setGeometry(QtCore.QRect(525, 211, 79, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_product_description.setFont(font)
        self.lbl_product_description.setObjectName("lbl_product_description")
        self.lbl_product_categories = QtWidgets.QLabel(Form)
        self.lbl_product_categories.setGeometry(QtCore.QRect(527, 380, 78, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_product_categories.setFont(font)
        self.lbl_product_categories.setObjectName("lbl_product_categories")
        self.btn_products_save = QtWidgets.QPushButton(Form)
        self.btn_products_save.setGeometry(QtCore.QRect(860, 500, 111, 51))
        self.btn_products_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_products_save.setObjectName("btn_products_save")
        self.lbl_product_name = QtWidgets.QLabel(Form)
        self.lbl_product_name.setGeometry(QtCore.QRect(559, 101, 48, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_product_name.setFont(font)
        self.lbl_product_name.setObjectName("lbl_product_name")
        self.pte_product_value = QtWidgets.QPlainTextEdit(Form)
        self.pte_product_value.setGeometry(QtCore.QRect(610, 300, 351, 31))
        self.pte_product_value.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pte_product_value.setObjectName("pte_product_value")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(10, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btn_products_back = QtWidgets.QPushButton(Form)
        self.btn_products_back.setGeometry(QtCore.QRect(30, 500, 111, 51))
        self.btn_products_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_products_back.setObjectName("btn_products_back")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_product_value = QtWidgets.QLabel(Form)
        self.lbl_product_value.setGeometry(QtCore.QRect(559, 308, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_product_value.setFont(font)
        self.lbl_product_value.setObjectName("lbl_product_value")
        self.btn_products_new = QtWidgets.QPushButton(Form)
        self.btn_products_new.setGeometry(QtCore.QRect(700, 500, 111, 51))
        self.btn_products_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_products_new.setObjectName("btn_products_new")
        self.pte_product_description = QtWidgets.QPlainTextEdit(Form)
        self.pte_product_description.setGeometry(QtCore.QRect(610, 150, 351, 121))
        self.pte_product_description.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pte_product_description.setObjectName("pte_product_description")
        self.cbx_product_categories = QtWidgets.QComboBox(Form)
        self.cbx_product_categories.setGeometry(QtCore.QRect(610, 370, 351, 41))
        self.cbx_product_categories.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbx_product_categories.setObjectName("cbx_product_categories")
        self.lbl_products = QtWidgets.QLabel(Form)
        self.lbl_products.setGeometry(QtCore.QRect(180, 50, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_products.setFont(font)
        self.lbl_products.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbl_products.setObjectName("lbl_products")
        self.vline1 = QtWidgets.QFrame(Form)
        self.vline1.setGeometry(QtCore.QRect(493, 0, 20, 461))
        self.vline1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline1.setObjectName("vline1")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(10, 0, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.lbl_product = QtWidgets.QLabel(Form)
        self.lbl_product.setGeometry(QtCore.QRect(730, 50, 100, 17))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_product.setFont(font)
        self.lbl_product.setObjectName("lbl_product")
        self.tbl_products = QtWidgets.QTableWidget(Form)
        self.tbl_products.setEnabled(True)
        self.tbl_products.setGeometry(QtCore.QRect(30, 80, 441, 361))
        self.tbl_products.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbl_products.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_products.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_products.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_products.setRowCount(0)
        self.tbl_products.setColumnCount(6)
        self.tbl_products.setObjectName("tbl_products")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        return self

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Produtos"))
        self.pte_product_name.setAccessibleName(_translate("Form", "pte_product_name"))
        self.pte_product_name.setPlaceholderText(_translate("Form", "Nome do produto..."))
        self.hline1.setAccessibleName(_translate("Form", "hline1"))
        self.lbl_product_description.setAccessibleName(_translate("Form", "lbl_product_description"))
        self.lbl_product_description.setText(_translate("Form", "Descrição"))
        self.lbl_product_categories.setText(_translate("Form", "Categoria"))
        self.btn_products_save.setAccessibleName(_translate("Form", "btn_products_save"))
        self.btn_products_save.setText(_translate("Form", "Salvar"))
        self.lbl_product_name.setAccessibleName(_translate("Form", "lbl_product_name"))
        self.lbl_product_name.setText(_translate("Form", "Nome"))
        self.pte_product_value.setAccessibleName(_translate("Form", "pte_product_value"))
        self.pte_product_value.setPlaceholderText(_translate("Form", "Valor unitário..."))
        self.btn_products_back.setAccessibleName(_translate("Form", "btn_products_back"))
        self.btn_products_back.setText(_translate("Form", "Voltar"))
        self.lbl_product_value.setAccessibleName(_translate("Form", "lbl_product_value"))
        self.lbl_product_value.setText(_translate("Form", "Valor"))
        self.btn_products_new.setAccessibleName(_translate("Form", "btn_products_new"))
        self.btn_products_new.setText(_translate("Form", "Novo"))
        self.pte_product_description.setAccessibleName(_translate("Form", "pte_product_description"))
        self.pte_product_description.setPlaceholderText(_translate("Form", "Descrição..."))
        self.cbx_product_categories.setAccessibleName(_translate("Form", "cbx_product_categories"))
        self.lbl_products.setToolTip(_translate("Form", "Lista de Produtos"))
        self.lbl_products.setAccessibleName(_translate("Form", "lbl_products"))
        self.lbl_products.setText(_translate("Form", "Produtos"))
        self.vline1.setAccessibleName(_translate("Form", "vline1"))
        self.lbl_product.setAccessibleName(_translate("Form", "lbl_product"))
        self.lbl_product.setText(_translate("Form", "Produto"))
        self.tbl_products.setAccessibleName(_translate("Form", "tbl_products"))
        self.tbl_products.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())