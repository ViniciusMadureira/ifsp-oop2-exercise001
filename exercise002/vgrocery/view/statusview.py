# This Python file uses the following encoding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from view.statusdialog import Ui_dlgStatus

class StatusView(Ui_dlgStatus):
    def __init__(self, parent, status, icon, text):
        super().__init__()
        self.initUi(parent, status, icon, text)

    def initUi(self, parent, status, icon, text):
        self.dialog = QtWidgets.QDialog(parent)
        self.setupUi(self.dialog)
        self.lblStatusIcon.setPixmap(QtGui.QPixmap(icon))
        self.lblStatusText.setText(text)
        self.btnBack.clicked.connect(self.btnBackClicked)
        self.center()
        self.dialog.show()

    def center(self):
        qr = self.dialog.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.dialog.move(qr.topLeft())

    def btnBackClicked(self):        
        self.dialog.close()
