# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lightapp\ui\QDesigner\MainWindow.ui'
#
# Created: Wed Dec 26 18:32:38 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 216)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "[*]LightApp", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 131))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.spinBox_show_nbSlots = QtGui.QSpinBox(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_show_nbSlots.sizePolicy().hasHeightForWidth())
        self.spinBox_show_nbSlots.setSizePolicy(sizePolicy)
        self.spinBox_show_nbSlots.setObjectName(_fromUtf8("spinBox_show_nbSlots"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_show_nbSlots)
        self.dateEdit_show_date = QtGui.QDateEdit(self.formLayoutWidget)
        self.dateEdit_show_date.setCalendarPopup(True)
        self.dateEdit_show_date.setObjectName(_fromUtf8("dateEdit_show_date"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.dateEdit_show_date)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Nom:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nb Circuits:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Auteur:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtBox_show_title = QtGui.QLineEdit(self.formLayoutWidget)
        self.txtBox_show_title.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtBox_show_title.setEchoMode(QtGui.QLineEdit.Normal)
        self.txtBox_show_title.setObjectName(_fromUtf8("txtBox_show_title"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtBox_show_title)
        self.txtBox_show_author = QtGui.QLineEdit(self.formLayoutWidget)
        self.txtBox_show_author.setObjectName(_fromUtf8("txtBox_show_author"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtBox_show_author)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 10, 81, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTest = QtGui.QMenu(self.menubar)
        self.menuTest.setTitle(QtGui.QApplication.translate("MainWindow", "&Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTest.setObjectName(_fromUtf8("menuTest"))
        self.menu_Export = QtGui.QMenu(self.menubar)
        self.menu_Export.setTitle(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Export.setObjectName(_fromUtf8("menu_Export"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_open = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/img/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon)
        self.action_open.setText(QtGui.QApplication.translate("MainWindow", "&Ouvrir...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ouvrir un spectacle existant", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_save = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/img/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon1)
        self.action_save.setText(QtGui.QApplication.translate("MainWindow", "&Enregistrer", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setStatusTip(QtGui.QApplication.translate("MainWindow", "Sauvegarder le spectacle en cours", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_save_as = QtGui.QAction(MainWindow)
        self.action_save_as.setIcon(icon1)
        self.action_save_as.setText(QtGui.QApplication.translate("MainWindow", "Enregistrer &Sous...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_as.setStatusTip(QtGui.QApplication.translate("MainWindow", "Sauvegarder le spectacle en cours", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_as.setObjectName(_fromUtf8("action_save_as"))
        self.action_new = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/img/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new.setIcon(icon2)
        self.action_new.setText(QtGui.QApplication.translate("MainWindow", "&Nouveau", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new.setStatusTip(QtGui.QApplication.translate("MainWindow", "Nouveau specatcle", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new.setObjectName(_fromUtf8("action_new"))
        self.menuTest.addAction(self.action_new)
        self.menuTest.addAction(self.action_open)
        self.menuTest.addAction(self.action_save)
        self.menuTest.addAction(self.action_save_as)
        self.menuTest.addSeparator()
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menu_Export.menuAction())
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtBox_show_title, self.spinBox_show_nbSlots)
        MainWindow.setTabOrder(self.spinBox_show_nbSlots, self.txtBox_show_author)
        MainWindow.setTabOrder(self.txtBox_show_author, self.dateEdit_show_date)

    def retranslateUi(self, MainWindow):
        pass

import ressources_rc
