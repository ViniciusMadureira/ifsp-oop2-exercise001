# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from view.confirmdialog import Ui_dlgConfirm

class ConfirmView(Ui_dlgConfirm):

    #result = -1

    def __init__(self, parent, icon, text):
        super().__init__()        
        self.initUi(parent, icon, text)
        
    def initUi(self, parent, icon, text):
        self.dialog = QtWidgets.QDialog(parent)
        self.setupUi(self.dialog)
        self.lblStatusIcon.setPixmap(QtGui.QPixmap(icon))
        self.lblStatusText.setText(text)
        self.btnCancel.clicked.connect(self.btnCancelClicked)
        self.btnOk.clicked.connect(self.btnOkClicked)
        self.center()
        self.dialog.exec()

    def center(self):
        qr = self.dialog.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.dialog.move(qr.topLeft())

    def btnCancelClicked(self):
        self.dialog.reject()

    def btnOkClicked(self):
        self.dialog.accept()

