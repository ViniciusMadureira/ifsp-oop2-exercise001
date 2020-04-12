# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgStatus(object):
    def setupUi(self, dlgStatus):
        dlgStatus.setObjectName("dlgStatus")
        dlgStatus.resize(400, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlgStatus.sizePolicy().hasHeightForWidth())
        dlgStatus.setSizePolicy(sizePolicy)
        dlgStatus.setMinimumSize(QtCore.QSize(400, 180))
        dlgStatus.setMaximumSize(QtCore.QSize(400, 180))
        dlgStatus.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgStatus.setWindowIcon(icon)
        dlgStatus.setStyleSheet("background-color: white")
        dlgStatus.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        dlgStatus.setModal(True)
        self.lblStatusText = QtWidgets.QLabel(dlgStatus)
        self.lblStatusText.setGeometry(QtCore.QRect(140, 20, 240, 90))
        self.lblStatusText.setMinimumSize(QtCore.QSize(240, 90))
        self.lblStatusText.setMaximumSize(QtCore.QSize(240, 90))
        self.lblStatusText.setBaseSize(QtCore.QSize(320, 90))
        self.lblStatusText.setTextFormat(QtCore.Qt.PlainText)
        self.lblStatusText.setWordWrap(True)
        self.lblStatusText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblStatusText.setObjectName("lblStatusText")
        self.lblStatusIcon = QtWidgets.QLabel(dlgStatus)
        self.lblStatusIcon.setGeometry(QtCore.QRect(20, 20, 100, 90))
        self.lblStatusIcon.setMinimumSize(QtCore.QSize(100, 90))
        self.lblStatusIcon.setMaximumSize(QtCore.QSize(100, 90))
        self.lblStatusIcon.setBaseSize(QtCore.QSize(100, 90))
        self.lblStatusIcon.setText("")
        self.lblStatusIcon.setTextFormat(QtCore.Qt.PlainText)
        self.lblStatusIcon.setPixmap(QtGui.QPixmap(":/dialog-ok_icon.png"))
        self.lblStatusIcon.setWordWrap(True)
        self.lblStatusIcon.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblStatusIcon.setObjectName("lblStatusIcon")
        self.btnBack = QtWidgets.QToolButton(dlgStatus)
        self.btnBack.setGeometry(QtCore.QRect(145, 120, 110, 50))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnBack.setFont(font)
        self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBack.setStyleSheet("background-color: #3b5998; color: white; font-weight: bold;  QToolTip{background-color: white}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon1)
        self.btnBack.setIconSize(QtCore.QSize(32, 32))
        self.btnBack.setShortcut("")
        self.btnBack.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnBack.setArrowType(QtCore.Qt.NoArrow)
        self.btnBack.setObjectName("btnBack")

        self.retranslateUi(dlgStatus)
        QtCore.QMetaObject.connectSlotsByName(dlgStatus)

    def retranslateUi(self, dlgStatus):
        _translate = QtCore.QCoreApplication.translate
        dlgStatus.setWindowTitle(_translate("dlgStatus", "Confirmação"))
        self.lblStatusText.setText(_translate("dlgStatus", "Objeto inserido com sucesso!"))
        self.btnBack.setToolTip(_translate("dlgStatus", "Voltar"))
        self.btnBack.setAccessibleName(_translate("dlgStatus", "btnProductsBack"))
        self.btnBack.setText(_translate("dlgStatus", "    OK"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgStatus = QtWidgets.QDialog()
    ui = Ui_dlgStatus()
    ui.setupUi(dlgStatus)
    dlgStatus.show()
    sys.exit(app.exec_())
