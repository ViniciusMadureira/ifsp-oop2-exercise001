# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productsform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmProducts(object):
    def setupUi(self, frmProducts):
        frmProducts.setObjectName("frmProducts")
        frmProducts.setWindowModality(QtCore.Qt.WindowModal)
        frmProducts.resize(980, 580)
        frmProducts.setMinimumSize(QtCore.QSize(980, 580))
        frmProducts.setMaximumSize(QtCore.QSize(980, 580))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmProducts.setWindowIcon(icon)
        frmProducts.setStyleSheet("background-color: white")
        frmProducts.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.pteProductName = QtWidgets.QPlainTextEdit(frmProducts)
        self.pteProductName.setGeometry(QtCore.QRect(610, 190, 350, 41))
        self.pteProductName.setStyleSheet("")
        self.pteProductName.setTabChangesFocus(True)
        self.pteProductName.setObjectName("pteProductName")
        self.hline1 = QtWidgets.QFrame(frmProducts)
        self.hline1.setGeometry(QtCore.QRect(0, 497, 991, 30))
        self.hline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline1.setObjectName("hline1")
        self.lblProductDescription = QtWidgets.QLabel(frmProducts)
        self.lblProductDescription.setGeometry(QtCore.QRect(506, 300, 98, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductDescription.setFont(font)
        self.lblProductDescription.setStyleSheet("color: #3b5998;")
        self.lblProductDescription.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProductDescription.setObjectName("lblProductDescription")
        self.lblProductCategories = QtWidgets.QLabel(frmProducts)
        self.lblProductCategories.setGeometry(QtCore.QRect(506, 460, 98, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductCategories.setFont(font)
        self.lblProductCategories.setStyleSheet("color: #3b5998;")
        self.lblProductCategories.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProductCategories.setObjectName("lblProductCategories")
        self.btnProductsSave = QtWidgets.QToolButton(frmProducts)
        self.btnProductsSave.setGeometry(QtCore.QRect(860, 520, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnProductsSave.setFont(font)
        self.btnProductsSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProductsSave.setStyleSheet("background-color: #3b5998; color: white; font-weight: bold")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProductsSave.setIcon(icon1)
        self.btnProductsSave.setIconSize(QtCore.QSize(32, 32))
        self.btnProductsSave.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnProductsSave.setObjectName("btnProductsSave")
        self.lblProductName = QtWidgets.QLabel(frmProducts)
        self.lblProductName.setGeometry(QtCore.QRect(506, 200, 98, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductName.setFont(font)
        self.lblProductName.setStyleSheet("color: #3b5998;")
        self.lblProductName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProductName.setObjectName("lblProductName")
        self.pteProductValue = QtWidgets.QPlainTextEdit(frmProducts)
        self.pteProductValue.setGeometry(QtCore.QRect(610, 390, 171, 41))
        self.pteProductValue.setStyleSheet("")
        self.pteProductValue.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pteProductValue.setTabChangesFocus(True)
        self.pteProductValue.setObjectName("pteProductValue")
        self.splitter = QtWidgets.QSplitter(frmProducts)
        self.splitter.setGeometry(QtCore.QRect(10, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btnProductsBack = QtWidgets.QToolButton(frmProducts)
        self.btnProductsBack.setGeometry(QtCore.QRect(30, 520, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnProductsBack.setFont(font)
        self.btnProductsBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProductsBack.setStyleSheet("background-color: #3b5998; color: white; font-weight: bold;  QToolTip{background-color: white}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProductsBack.setIcon(icon2)
        self.btnProductsBack.setIconSize(QtCore.QSize(32, 32))
        self.btnProductsBack.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnProductsBack.setArrowType(QtCore.Qt.NoArrow)
        self.btnProductsBack.setObjectName("btnProductsBack")
        self.layoutWidget = QtWidgets.QWidget(frmProducts)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblProductValue = QtWidgets.QLabel(frmProducts)
        self.lblProductValue.setGeometry(QtCore.QRect(506, 400, 98, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductValue.setFont(font)
        self.lblProductValue.setStyleSheet("color: #3b5998;")
        self.lblProductValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProductValue.setObjectName("lblProductValue")
        self.btnProductsNew = QtWidgets.QToolButton(frmProducts)
        self.btnProductsNew.setGeometry(QtCore.QRect(700, 520, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnProductsNew.setFont(font)
        self.btnProductsNew.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProductsNew.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProductsNew.setAutoFillBackground(False)
        self.btnProductsNew.setStyleSheet("background-color: #3b5998; color: white; font-weight: bold")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/new_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProductsNew.setIcon(icon3)
        self.btnProductsNew.setIconSize(QtCore.QSize(32, 32))
        self.btnProductsNew.setCheckable(False)
        self.btnProductsNew.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnProductsNew.setObjectName("btnProductsNew")
        self.pteProductDescription = QtWidgets.QPlainTextEdit(frmProducts)
        self.pteProductDescription.setGeometry(QtCore.QRect(610, 250, 350, 121))
        self.pteProductDescription.setStyleSheet("")
        self.pteProductDescription.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pteProductDescription.setTabChangesFocus(True)
        self.pteProductDescription.setObjectName("pteProductDescription")
        self.cbxProductCategories = QtWidgets.QComboBox(frmProducts)
        self.cbxProductCategories.setGeometry(QtCore.QRect(610, 450, 301, 41))
        self.cbxProductCategories.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbxProductCategories.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cbxProductCategories.setStyleSheet("color: black;\n"
"background-color: white;\n"
"selection-background-color: #3b5998;\n"
"selection-color: white;\n"
"")
        self.cbxProductCategories.setEditable(False)
        self.cbxProductCategories.setObjectName("cbxProductCategories")
        self.lblProducts = QtWidgets.QLabel(frmProducts)
        self.lblProducts.setGeometry(QtCore.QRect(0, 28, 501, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblProducts.setFont(font)
        self.lblProducts.setStyleSheet("color: #3b5998;")
        self.lblProducts.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProducts.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblProducts.setObjectName("lblProducts")
        self.vline1 = QtWidgets.QFrame(frmProducts)
        self.vline1.setGeometry(QtCore.QRect(493, 0, 20, 511))
        self.vline1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline1.setObjectName("vline1")
        self.splitter_2 = QtWidgets.QSplitter(frmProducts)
        self.splitter_2.setGeometry(QtCore.QRect(10, 0, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.lblProduct = QtWidgets.QLabel(frmProducts)
        self.lblProduct.setGeometry(QtCore.QRect(503, 28, 476, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblProduct.setFont(font)
        self.lblProduct.setStyleSheet("color: #3b5998;")
        self.lblProduct.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProduct.setObjectName("lblProduct")
        self.tblProducts = QtWidgets.QTableWidget(frmProducts)
        self.tblProducts.setEnabled(True)
        self.tblProducts.setGeometry(QtCore.QRect(30, 100, 440, 401))
        self.tblProducts.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tblProducts.setStyleSheet("alternate-background-color: #f7b88b;\n"
"background-color: white;\n"
"selection-background-color: #3b5998;\n"
"selection-color: white;")
        self.tblProducts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblProducts.setAlternatingRowColors(True)
        self.tblProducts.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblProducts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblProducts.setRowCount(0)
        self.tblProducts.setColumnCount(8)
        self.tblProducts.setObjectName("tblProducts")
        self.tblProducts.verticalHeader().setVisible(False)
        self.btnProductsDelete = QtWidgets.QToolButton(frmProducts)
        self.btnProductsDelete.setGeometry(QtCore.QRect(540, 520, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnProductsDelete.setFont(font)
        self.btnProductsDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProductsDelete.setStatusTip("")
        self.btnProductsDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProductsDelete.setAutoFillBackground(False)
        self.btnProductsDelete.setStyleSheet("background-color: #3b5998; color: white; font-weight: bold")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProductsDelete.setIcon(icon4)
        self.btnProductsDelete.setIconSize(QtCore.QSize(32, 32))
        self.btnProductsDelete.setCheckable(False)
        self.btnProductsDelete.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnProductsDelete.setObjectName("btnProductsDelete")
        self.lblTblProductsEmpty = QtWidgets.QLabel(frmProducts)
        self.lblTblProductsEmpty.setGeometry(QtCore.QRect(50, 160, 401, 291))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblTblProductsEmpty.setFont(font)
        self.lblTblProductsEmpty.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lblTblProductsEmpty.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTblProductsEmpty.setWordWrap(True)
        self.lblTblProductsEmpty.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblTblProductsEmpty.setObjectName("lblTblProductsEmpty")
        self.lblProductImage = QtWidgets.QLabel(frmProducts)
        self.lblProductImage.setGeometry(QtCore.QRect(506, 111, 98, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductImage.setFont(font)
        self.lblProductImage.setStyleSheet("color: #3b5998;")
        self.lblProductImage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProductImage.setWordWrap(False)
        self.lblProductImage.setObjectName("lblProductImage")
        self.btnProductPicture = QtWidgets.QToolButton(frmProducts)
        self.btnProductPicture.setGeometry(QtCore.QRect(610, 71, 120, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProductPicture.sizePolicy().hasHeightForWidth())
        self.btnProductPicture.setSizePolicy(sizePolicy)
        self.btnProductPicture.setMinimumSize(QtCore.QSize(120, 100))
        self.btnProductPicture.setMaximumSize(QtCore.QSize(120, 100))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnProductPicture.setFont(font)
        self.btnProductPicture.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProductPicture.setAutoFillBackground(False)
        self.btnProductPicture.setStyleSheet("")
        self.btnProductPicture.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/defaultimage_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProductPicture.setIcon(icon5)
        self.btnProductPicture.setIconSize(QtCore.QSize(256, 256))
        self.btnProductPicture.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnProductPicture.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnProductPicture.setAutoRaise(False)
        self.btnProductPicture.setArrowType(QtCore.Qt.NoArrow)
        self.btnProductPicture.setObjectName("btnProductPicture")
        self.btnCategoriesNew = QtWidgets.QToolButton(frmProducts)
        self.btnCategoriesNew.setGeometry(QtCore.QRect(920, 450, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnCategoriesNew.setFont(font)
        self.btnCategoriesNew.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCategoriesNew.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnCategoriesNew.setAutoFillBackground(False)
        self.btnCategoriesNew.setIcon(icon3)
        self.btnCategoriesNew.setIconSize(QtCore.QSize(32, 32))
        self.btnCategoriesNew.setCheckable(False)
        self.btnCategoriesNew.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnCategoriesNew.setAutoRaise(True)
        self.btnCategoriesNew.setObjectName("btnCategoriesNew")
        self.btnProductPictureDelete = QtWidgets.QToolButton(frmProducts)
        self.btnProductPictureDelete.setGeometry(QtCore.QRect(740, 101, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnProductPictureDelete.setFont(font)
        self.btnProductPictureDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProductPictureDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProductPictureDelete.setAutoFillBackground(False)
        self.btnProductPictureDelete.setText("")
        self.btnProductPictureDelete.setIcon(icon4)
        self.btnProductPictureDelete.setIconSize(QtCore.QSize(32, 32))
        self.btnProductPictureDelete.setCheckable(False)
        self.btnProductPictureDelete.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnProductPictureDelete.setAutoRaise(True)
        self.btnProductPictureDelete.setObjectName("btnProductPictureDelete")
        self.lblProductNameValidation = QtWidgets.QLabel(frmProducts)
        self.lblProductNameValidation.setGeometry(QtCore.QRect(610, 230, 350, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductNameValidation.setFont(font)
        self.lblProductNameValidation.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblProductNameValidation.setToolTip("")
        self.lblProductNameValidation.setStyleSheet("color: darkred")
        self.lblProductNameValidation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblProductNameValidation.setObjectName("lblProductNameValidation")
        self.lblProductDescriptionValidation = QtWidgets.QLabel(frmProducts)
        self.lblProductDescriptionValidation.setGeometry(QtCore.QRect(610, 370, 350, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductDescriptionValidation.setFont(font)
        self.lblProductDescriptionValidation.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblProductDescriptionValidation.setToolTip("")
        self.lblProductDescriptionValidation.setStyleSheet("color: darkred")
        self.lblProductDescriptionValidation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblProductDescriptionValidation.setObjectName("lblProductDescriptionValidation")
        self.lblProductValueValidation = QtWidgets.QLabel(frmProducts)
        self.lblProductValueValidation.setGeometry(QtCore.QRect(610, 430, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductValueValidation.setFont(font)
        self.lblProductValueValidation.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblProductValueValidation.setToolTip("")
        self.lblProductValueValidation.setStyleSheet("color: darkred;")
        self.lblProductValueValidation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblProductValueValidation.setObjectName("lblProductValueValidation")
        self.lblProductAmount = QtWidgets.QLabel(frmProducts)
        self.lblProductAmount.setGeometry(QtCore.QRect(783, 400, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductAmount.setFont(font)
        self.lblProductAmount.setStyleSheet("color: #3b5998;")
        self.lblProductAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProductAmount.setObjectName("lblProductAmount")
        self.pteProductAmount = QtWidgets.QPlainTextEdit(frmProducts)
        self.pteProductAmount.setGeometry(QtCore.QRect(870, 390, 91, 41))
        self.pteProductAmount.setStyleSheet("")
        self.pteProductAmount.setMidLineWidth(0)
        self.pteProductAmount.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pteProductAmount.setTabChangesFocus(True)
        self.pteProductAmount.setObjectName("pteProductAmount")
        self.lblProductAmountValidation = QtWidgets.QLabel(frmProducts)
        self.lblProductAmountValidation.setGeometry(QtCore.QRect(870, 430, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductAmountValidation.setFont(font)
        self.lblProductAmountValidation.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblProductAmountValidation.setToolTip("")
        self.lblProductAmountValidation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblProductAmountValidation.setStyleSheet("color: darkred")
        self.lblProductAmountValidation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblProductAmountValidation.setObjectName("lblProductAmountValidation")
        self.pteProductsSearch = QtWidgets.QPlainTextEdit(frmProducts)
        self.pteProductsSearch.setGeometry(QtCore.QRect(30, 60, 440, 31))
        self.pteProductsSearch.setStyleSheet("")
        self.pteProductsSearch.setTabChangesFocus(True)
        self.pteProductsSearch.setObjectName("pteProductsSearch")
        self.btnProductsSearchClear = QtWidgets.QToolButton(frmProducts)
        self.btnProductsSearchClear.setGeometry(QtCore.QRect(443, 63, 24, 24))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnProductsSearchClear.setFont(font)
        self.btnProductsSearchClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProductsSearchClear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProductsSearchClear.setAutoFillBackground(False)
        self.btnProductsSearchClear.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/clear-search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProductsSearchClear.setIcon(icon6)
        self.btnProductsSearchClear.setIconSize(QtCore.QSize(24, 24))
        self.btnProductsSearchClear.setCheckable(False)
        self.btnProductsSearchClear.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnProductsSearchClear.setAutoRaise(True)
        self.btnProductsSearchClear.setObjectName("btnProductsSearchClear")
        self.lblProductId = QtWidgets.QLabel(frmProducts)
        self.lblProductId.setGeometry(QtCore.QRect(866, 71, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductId.setFont(font)
        self.lblProductId.setToolTip("")
        self.lblProductId.setStyleSheet("color: #3b5998;")
        self.lblProductId.setText("")
        self.lblProductId.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProductId.setWordWrap(False)
        self.lblProductId.setObjectName("lblProductId")
        self.lblProductPicturePath = QtWidgets.QLabel(frmProducts)
        self.lblProductPicturePath.setGeometry(QtCore.QRect(866, 111, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductPicturePath.setFont(font)
        self.lblProductPicturePath.setToolTip("")
        self.lblProductPicturePath.setStyleSheet("color: #3b5998;")
        self.lblProductPicturePath.setText("")
        self.lblProductPicturePath.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProductPicturePath.setWordWrap(False)
        self.lblProductPicturePath.setObjectName("lblProductPicturePath")
        self.lblProductCategoriesValidation = QtWidgets.QLabel(frmProducts)
        self.lblProductCategoriesValidation.setGeometry(QtCore.QRect(610, 491, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblProductCategoriesValidation.setFont(font)
        self.lblProductCategoriesValidation.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lblProductCategoriesValidation.setToolTip("")
        self.lblProductCategoriesValidation.setStyleSheet("color: darkred;")
        self.lblProductCategoriesValidation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblProductCategoriesValidation.setObjectName("lblProductCategoriesValidation")
        self.tblProducts.raise_()
        self.lblTblProductsEmpty.raise_()
        self.pteProductName.raise_()
        self.hline1.raise_()
        self.lblProductDescription.raise_()
        self.lblProductCategories.raise_()
        self.btnProductsSave.raise_()
        self.lblProductName.raise_()
        self.pteProductValue.raise_()
        self.splitter.raise_()
        self.btnProductsBack.raise_()
        self.layoutWidget.raise_()
        self.lblProductValue.raise_()
        self.btnProductsNew.raise_()
        self.pteProductDescription.raise_()
        self.cbxProductCategories.raise_()
        self.lblProducts.raise_()
        self.vline1.raise_()
        self.splitter_2.raise_()
        self.lblProduct.raise_()
        self.btnProductsDelete.raise_()
        self.lblProductImage.raise_()
        self.btnProductPicture.raise_()
        self.btnCategoriesNew.raise_()
        self.btnProductPictureDelete.raise_()
        self.lblProductNameValidation.raise_()
        self.lblProductDescriptionValidation.raise_()
        self.lblProductValueValidation.raise_()
        self.lblProductAmount.raise_()
        self.pteProductAmount.raise_()
        self.lblProductAmountValidation.raise_()
        self.pteProductsSearch.raise_()
        self.btnProductsSearchClear.raise_()
        self.lblProductId.raise_()
        self.lblProductPicturePath.raise_()
        self.lblProductCategoriesValidation.raise_()

        self.retranslateUi(frmProducts)
        QtCore.QMetaObject.connectSlotsByName(frmProducts)
        frmProducts.setTabOrder(self.btnProductPicture, self.btnProductPictureDelete)
        frmProducts.setTabOrder(self.btnProductPictureDelete, self.pteProductName)
        frmProducts.setTabOrder(self.pteProductName, self.pteProductDescription)
        frmProducts.setTabOrder(self.pteProductDescription, self.pteProductValue)
        frmProducts.setTabOrder(self.pteProductValue, self.pteProductAmount)
        frmProducts.setTabOrder(self.pteProductAmount, self.cbxProductCategories)
        frmProducts.setTabOrder(self.cbxProductCategories, self.btnCategoriesNew)
        frmProducts.setTabOrder(self.btnCategoriesNew, self.btnProductsSave)
        frmProducts.setTabOrder(self.btnProductsSave, self.btnProductsNew)
        frmProducts.setTabOrder(self.btnProductsNew, self.btnProductsDelete)
        frmProducts.setTabOrder(self.btnProductsDelete, self.btnProductsBack)
        frmProducts.setTabOrder(self.btnProductsBack, self.tblProducts)

    def retranslateUi(self, frmProducts):
        _translate = QtCore.QCoreApplication.translate
        frmProducts.setWindowTitle(_translate("frmProducts", "Produtos"))
        frmProducts.setAccessibleName(_translate("frmProducts", "frmProducts"))
        self.pteProductName.setToolTip(_translate("frmProducts", "Nome do Produto"))
        self.pteProductName.setAccessibleName(_translate("frmProducts", "pteProductName"))
        self.pteProductName.setPlaceholderText(_translate("frmProducts", "Nome do produto..."))
        self.hline1.setAccessibleName(_translate("frmProducts", "hline1"))
        self.lblProductDescription.setToolTip(_translate("frmProducts", "Descrição do Produto"))
        self.lblProductDescription.setAccessibleName(_translate("frmProducts", "lblProductDescription"))
        self.lblProductDescription.setText(_translate("frmProducts", "Descrição"))
        self.lblProductCategories.setToolTip(_translate("frmProducts", "Categoria do Produto"))
        self.lblProductCategories.setAccessibleName(_translate("frmProducts", "lblProductCategories"))
        self.lblProductCategories.setText(_translate("frmProducts", "Categoria*"))
        self.btnProductsSave.setToolTip(_translate("frmProducts", "Salvar Produto"))
        self.btnProductsSave.setAccessibleName(_translate("frmProducts", "btnProductsSave"))
        self.btnProductsSave.setText(_translate("frmProducts", " Salvar"))
        self.btnProductsSave.setShortcut(_translate("frmProducts", "Ctrl+S"))
        self.lblProductName.setToolTip(_translate("frmProducts", "Nome do Produto"))
        self.lblProductName.setAccessibleName(_translate("frmProducts", "lblProductName"))
        self.lblProductName.setText(_translate("frmProducts", "Nome*"))
        self.pteProductValue.setToolTip(_translate("frmProducts", "Valor Unitário do Produto"))
        self.pteProductValue.setAccessibleName(_translate("frmProducts", "pteProductValue"))
        self.pteProductValue.setPlainText(_translate("frmProducts", "R$0,00"))
        self.pteProductValue.setPlaceholderText(_translate("frmProducts", "Valor unitário do produto..."))
        self.btnProductsBack.setToolTip(_translate("frmProducts", "Voltar para Janela Principal"))
        self.btnProductsBack.setAccessibleName(_translate("frmProducts", "btnProductsBack"))
        self.btnProductsBack.setText(_translate("frmProducts", " Voltar"))
        self.btnProductsBack.setShortcut(_translate("frmProducts", "Ctrl+B"))
        self.lblProductValue.setToolTip(_translate("frmProducts", "Valor Unitário do Produto"))
        self.lblProductValue.setAccessibleName(_translate("frmProducts", "lblProductValue"))
        self.lblProductValue.setText(_translate("frmProducts", "Valor*"))
        self.btnProductsNew.setToolTip(_translate("frmProducts", "Novo Produto"))
        self.btnProductsNew.setAccessibleName(_translate("frmProducts", "btnProductsNew"))
        self.btnProductsNew.setText(_translate("frmProducts", " Novo"))
        self.btnProductsNew.setShortcut(_translate("frmProducts", "Ctrl+N"))
        self.pteProductDescription.setToolTip(_translate("frmProducts", "Descrição do Produto"))
        self.pteProductDescription.setAccessibleName(_translate("frmProducts", "pteProductDescription"))
        self.pteProductDescription.setPlaceholderText(_translate("frmProducts", "Descrição do produto..."))
        self.cbxProductCategories.setToolTip(_translate("frmProducts", "Categoria do Produto"))
        self.cbxProductCategories.setAccessibleName(_translate("frmProducts", "cbxProductCategories"))
        self.lblProducts.setToolTip(_translate("frmProducts", "Lista de Produtos"))
        self.lblProducts.setAccessibleName(_translate("frmProducts", "lblProducts"))
        self.lblProducts.setText(_translate("frmProducts", "Produtos"))
        self.vline1.setAccessibleName(_translate("frmProducts", "vline1"))
        self.lblProduct.setToolTip(_translate("frmProducts", "Cadastro de Produtos"))
        self.lblProduct.setAccessibleName(_translate("frmProducts", "lblProduct"))
        self.lblProduct.setText(_translate("frmProducts", "Cadastro"))
        self.tblProducts.setAccessibleName(_translate("frmProducts", "tblProducts"))
        self.tblProducts.setSortingEnabled(True)
        self.btnProductsDelete.setToolTip(_translate("frmProducts", "Apagar Produto"))
        self.btnProductsDelete.setAccessibleName(_translate("frmProducts", "btnProductsDelete"))
        self.btnProductsDelete.setText(_translate("frmProducts", "Apagar"))
        self.btnProductsDelete.setShortcut(_translate("frmProducts", "Ctrl+D"))
        self.lblTblProductsEmpty.setToolTip(_translate("frmProducts", "Nenhum registro encontrado!"))
        self.lblTblProductsEmpty.setAccessibleName(_translate("frmProducts", "lblTblProductsEmpty"))
        self.lblTblProductsEmpty.setText(_translate("frmProducts", "Nenhum registro encontrado!"))
        self.lblProductImage.setToolTip(_translate("frmProducts", "Imagem do Produto"))
        self.lblProductImage.setAccessibleName(_translate("frmProducts", "lblProductImage"))
        self.lblProductImage.setText(_translate("frmProducts", "Imagem"))
        self.btnProductPicture.setToolTip(_translate("frmProducts", "Imagem do Produto"))
        self.btnProductPicture.setAccessibleName(_translate("frmProducts", "btnProductPicture"))
        self.btnProductPicture.setShortcut(_translate("frmProducts", "Ctrl+I"))
        self.btnCategoriesNew.setToolTip(_translate("frmProducts", "Nova Categoria"))
        self.btnCategoriesNew.setAccessibleName(_translate("frmProducts", "btnCategoriesNew"))
        self.btnCategoriesNew.setText(_translate("frmProducts", " Novo"))
        self.btnCategoriesNew.setShortcut(_translate("frmProducts", "Ctrl+G"))
        self.btnProductPictureDelete.setToolTip(_translate("frmProducts", "Remover Imagem"))
        self.btnProductPictureDelete.setAccessibleName(_translate("frmProducts", "btnProductPictureDelete"))
        self.lblProductNameValidation.setAccessibleName(_translate("frmProducts", "lblProductNameValidation"))
        self.lblProductNameValidation.setText(_translate("frmProducts", "Insira um nome com tamanho de 2 a 100 caracteres."))
        self.lblProductDescriptionValidation.setAccessibleName(_translate("frmProducts", "lblProductDescriptionValidation"))
        self.lblProductDescriptionValidation.setText(_translate("frmProducts", "Insira uma descrição com tamanho de 2 a 400 caracteres."))
        self.lblProductValueValidation.setAccessibleName(_translate("frmProducts", "lblProductValueValidation"))
        self.lblProductValueValidation.setText(_translate("frmProducts", "De R$0,00 a R$100.000,00."))
        self.lblProductAmount.setToolTip(_translate("frmProducts", "Quantidade do Produto em Estoque"))
        self.lblProductAmount.setAccessibleName(_translate("frmProducts", "lblProductAmount"))
        self.lblProductAmount.setText(_translate("frmProducts", "Estoque*"))
        self.pteProductAmount.setToolTip(_translate("frmProducts", "Quantidade do Produto em Estoque"))
        self.pteProductAmount.setAccessibleName(_translate("frmProducts", "pteProductAmount"))
        self.pteProductAmount.setPlainText(_translate("frmProducts", "0"))
        self.pteProductAmount.setPlaceholderText(_translate("frmProducts", "Qtd. em Estoque..."))
        self.lblProductAmountValidation.setAccessibleName(_translate("frmProducts", "lblProductAmountValidation"))
        self.lblProductAmountValidation.setText(_translate("frmProducts", "De 0 a 1000."))
        self.pteProductsSearch.setToolTip(_translate("frmProducts", "Buscar Produto"))
        self.pteProductsSearch.setAccessibleName(_translate("frmProducts", "pteProductName"))
        self.pteProductsSearch.setPlaceholderText(_translate("frmProducts", "Buscar produto..."))
        self.btnProductsSearchClear.setToolTip(_translate("frmProducts", "Apagar Busca"))
        self.btnProductsSearchClear.setAccessibleName(_translate("frmProducts", "btnProductsSearchClear"))
        self.lblProductId.setAccessibleName(_translate("frmProducts", "lblProductId"))
        self.lblProductPicturePath.setAccessibleName(_translate("frmProducts", "lblProductPicturePath"))
        self.lblProductCategoriesValidation.setAccessibleName(_translate("frmProducts", "lblProductCategoriesValidation"))
        self.lblProductCategoriesValidation.setText(_translate("frmProducts", "Selecione uma categoria."))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmProducts = QtWidgets.QWidget()
    ui = Ui_frmProducts()
    ui.setupUi(frmProducts)
    frmProducts.show()
    sys.exit(app.exec_())
