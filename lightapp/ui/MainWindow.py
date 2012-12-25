# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lightapp\ui\QDesigner\MainWindow.ui'
#
# Created: Tue Dec 25 16:54:32 2012
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
        MainWindow.resize(400, 286)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LightApp", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Spectacles", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.table_shows = QtGui.QTableWidget(self.formLayoutWidget)
        self.table_shows.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_shows.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_shows.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_shows.setShowGrid(False)
        self.table_shows.setColumnCount(3)
        self.table_shows.setObjectName(_fromUtf8("table_shows"))
        self.table_shows.setRowCount(0)
        self.table_shows.horizontalHeader().setVisible(False)
        self.table_shows.verticalHeader().setVisible(False)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.table_shows)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_new = QtGui.QPushButton(self.formLayoutWidget)
        self.btn_new.setText(QtGui.QApplication.translate("MainWindow", "Nouveau", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new.setObjectName(_fromUtf8("btn_new"))
        self.horizontalLayout_2.addWidget(self.btn_new)
        self.btn_gen_csv = QtGui.QPushButton(self.formLayoutWidget)
        self.btn_gen_csv.setEnabled(False)
        self.btn_gen_csv.setText(QtGui.QApplication.translate("MainWindow", "Export CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_gen_csv.setObjectName(_fromUtf8("btn_gen_csv"))
        self.horizontalLayout_2.addWidget(self.btn_gen_csv)
        self.btn_gen_pdf = QtGui.QPushButton(self.formLayoutWidget)
        self.btn_gen_pdf.setEnabled(False)
        self.btn_gen_pdf.setText(QtGui.QApplication.translate("MainWindow", "Export PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_gen_pdf.setObjectName(_fromUtf8("btn_gen_pdf"))
        self.horizontalLayout_2.addWidget(self.btn_gen_pdf)
        self.formLayout.setLayout(3, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_2)
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

