# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lightapp\ui\QDesigner\DlgInfos.ui'
#
# Created: Tue Dec 25 17:54:07 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dlg_show_infos(object):
    def setupUi(self, dlg_show_infos):
        dlg_show_infos.setObjectName(_fromUtf8("dlg_show_infos"))
        dlg_show_infos.setWindowModality(QtCore.Qt.WindowModal)
        dlg_show_infos.resize(269, 199)
        dlg_show_infos.setWindowTitle(QtGui.QApplication.translate("dlg_show_infos", "Infos générales", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(dlg_show_infos)
        self.buttonBox.setGeometry(QtCore.QRect(60, 160, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(dlg_show_infos)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 247, 141))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("dlg_show_infos", "Nom:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setText(QtGui.QApplication.translate("dlg_show_infos", "Nb Circuits:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setText(QtGui.QApplication.translate("dlg_show_infos", "Auteur:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setText(QtGui.QApplication.translate("dlg_show_infos", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.txtBox_show_title = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtBox_show_title.setObjectName(_fromUtf8("txtBox_show_title"))
        self.gridLayout.addWidget(self.txtBox_show_title, 0, 2, 1, 1)
        self.txtBox_show_author = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtBox_show_author.setObjectName(_fromUtf8("txtBox_show_author"))
        self.gridLayout.addWidget(self.txtBox_show_author, 2, 2, 1, 1)
        self.spinBox_show_nbSlots = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox_show_nbSlots.setObjectName(_fromUtf8("spinBox_show_nbSlots"))
        self.gridLayout.addWidget(self.spinBox_show_nbSlots, 1, 2, 1, 1)
        self.dateEdit_show_date = QtGui.QDateEdit(self.gridLayoutWidget)
        self.dateEdit_show_date.setCalendarPopup(True)
        self.dateEdit_show_date.setObjectName(_fromUtf8("dateEdit_show_date"))
        self.gridLayout.addWidget(self.dateEdit_show_date, 3, 2, 1, 1)

        self.retranslateUi(dlg_show_infos)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dlg_show_infos.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dlg_show_infos.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_show_infos)

    def retranslateUi(self, dlg_show_infos):
        pass

