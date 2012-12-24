# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lightapp\ui\QDesigner\MainWindow.ui'
#
# Created: Tue Dec 25 00:22:55 2012
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
        MainWindow.resize(400, 337)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LightApp", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_new = QtGui.QPushButton(self.centralwidget)
        self.btn_new.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.btn_new.setText(QtGui.QApplication.translate("MainWindow", "Nouveau", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new.setObjectName(_fromUtf8("btn_new"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Spectacles", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 381, 192))
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTest = QtGui.QMenu(self.menubar)
        self.menuTest.setTitle(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTest.setObjectName(_fromUtf8("menuTest"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionMenu = QtGui.QAction(MainWindow)
        self.actionMenu.setText(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMenu.setObjectName(_fromUtf8("actionMenu"))
        self.menuTest.addAction(self.actionMenu)
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

