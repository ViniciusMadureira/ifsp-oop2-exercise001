# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgConfirm(object):
    def setupUi(self, dlgConfirm):
        dlgConfirm.setObjectName("dlgConfirm")
        dlgConfirm.resize(400, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlgConfirm.sizePolicy().hasHeightForWidth())
        dlgConfirm.setSizePolicy(sizePolicy)
        dlgConfirm.setMinimumSize(QtCore.QSize(400, 180))
        dlgConfirm.setMaximumSize(QtCore.QSize(400, 180))
        dlgConfirm.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgConfirm.setWindowIcon(icon)
        dlgConfirm.setStyleSheet("background-color: white")
        dlgConfirm.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        dlgConfirm.setModal(True)
        self.lblStatusText = QtWidgets.QLabel(dlgConfirm)
        self.lblStatusText.setGeometry(QtCore.QRect(140, 20, 240, 100))
        self.lblStatusText.setMinimumSize(QtCore.QSize(240, 100))
        self.lblStatusText.setMaximumSize(QtCore.QSize(240, 100))
        self.lblStatusText.setBaseSize(QtCore.QSize(240, 100))
        self.lblStatusText.setTextFormat(QtCore.Qt.PlainText)
        self.lblStatusText.setWordWrap(True)
        self.lblStatusText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblStatusText.setObjectName("lblStatusText")
        self.lblStatusIcon = QtWidgets.QLabel(dlgConfirm)
        self.lblStatusIcon.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.lblStatusIcon.setMinimumSize(QtCore.QSize(100, 100))
        self.lblStatusIcon.setMaximumSize(QtCore.QSize(100, 100))
        self.lblStatusIcon.setBaseSize(QtCore.QSize(100, 100))
        self.lblStatusIcon.setText("")
        self.lblStatusIcon.setTextFormat(QtCore.Qt.PlainText)
        self.lblStatusIcon.setPixmap(QtGui.QPixmap(":/dialog-confirm_icon.png"))
        self.lblStatusIcon.setWordWrap(True)
        self.lblStatusIcon.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblStatusIcon.setObjectName("lblStatusIcon")
        self.btnOk = QtWidgets.QToolButton(dlgConfirm)
        self.btnOk.setGeometry(QtCore.QRect(280, 140, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOk.setStyleSheet("background-color: #3b5998; color: white; font-weight: bold;  QToolTip{background-color: white}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/dialog-ok_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon1)
        self.btnOk.setIconSize(QtCore.QSize(32, 32))
        self.btnOk.setShortcut("")
        self.btnOk.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnOk.setArrowType(QtCore.Qt.NoArrow)
        self.btnOk.setObjectName("btnOk")
        self.btnCancel = QtWidgets.QToolButton(dlgConfirm)
        self.btnCancel.setGeometry(QtCore.QRect(140, 140, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("background-color: #3b5998; color: white; font-weight: bold;  QToolTip{background-color: white}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dialog-cancel_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon2)
        self.btnCancel.setIconSize(QtCore.QSize(24, 24))
        self.btnCancel.setShortcut("")
        self.btnCancel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnCancel.setArrowType(QtCore.Qt.NoArrow)
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(dlgConfirm)
        QtCore.QMetaObject.connectSlotsByName(dlgConfirm)

    def retranslateUi(self, dlgConfirm):
        _translate = QtCore.QCoreApplication.translate
        dlgConfirm.setWindowTitle(_translate("dlgConfirm", "Confirmação"))
        self.lblStatusText.setText(_translate("dlgConfirm", "Tem certeza de que deseja remover este produto permanentemente?"))
        self.btnOk.setToolTip(_translate("dlgConfirm", "Confirmar"))
        self.btnOk.setAccessibleName(_translate("dlgConfirm", "btnOk"))
        self.btnOk.setText(_translate("dlgConfirm", "   OK"))
        self.btnCancel.setToolTip(_translate("dlgConfirm", "Cancelar"))
        self.btnCancel.setAccessibleName(_translate("dlgConfirm", "btnCancel"))
        self.btnCancel.setText(_translate("dlgConfirm", "Cancelar"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgConfirm = QtWidgets.QDialog()
    ui = Ui_dlgConfirm()
    ui.setupUi(dlgConfirm)
    dlgConfirm.show()
    sys.exit(app.exec_())
