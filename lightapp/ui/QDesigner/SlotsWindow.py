# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lightapp\ui\QDesigner\SlotsWindow.ui'
#
# Created: Fri Jan  4 20:53:08 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(569, 371)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "LightApp - Mémoires", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 551, 351))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.slots_scroller = QtGui.QScrollArea(self.verticalLayoutWidget_2)
        self.slots_scroller.setWidgetResizable(True)
        self.slots_scroller.setObjectName(_fromUtf8("slots_scroller"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 547, 316))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 551, 321))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.scroller_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.scroller_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.scroller_layout.setMargin(0)
        self.scroller_layout.setObjectName(_fromUtf8("scroller_layout"))
        self.slots_scroller.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.slots_scroller)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_add_slot = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.btn_add_slot.setText(QtGui.QApplication.translate("Dialog", "Nouveau \"Slot\"", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_slot.setObjectName(_fromUtf8("btn_add_slot"))
        self.horizontalLayout.addWidget(self.btn_add_slot)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget_2)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

