# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lightapp\ui\QDesigner\SlotWidget.ui'
#
# Created: Sun Dec 30 14:33:25 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SlotWidget(object):
    def setupUi(self, SlotWidget):
        SlotWidget.setObjectName(_fromUtf8("SlotWidget"))
        SlotWidget.resize(548, 153)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SlotWidget.sizePolicy().hasHeightForWidth())
        SlotWidget.setSizePolicy(sizePolicy)
        SlotWidget.setMinimumSize(QtCore.QSize(399, 153))
        SlotWidget.setWindowTitle(QtGui.QApplication.translate("SlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.frame = QtGui.QFrame(SlotWidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 551, 31))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border: {solid 5px red};"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 511, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(QtGui.QApplication.translate("SlotWidget", "In:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_2 = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText(QtGui.QApplication.translate("SlotWidget", "Out:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.txtBox_slot_id = QtGui.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtBox_slot_id.sizePolicy().hasHeightForWidth())
        self.txtBox_slot_id.setSizePolicy(sizePolicy)
        self.txtBox_slot_id.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txtBox_slot_id.setAlignment(QtCore.Qt.AlignCenter)
        self.txtBox_slot_id.setObjectName(_fromUtf8("txtBox_slot_id"))
        self.horizontalLayout.addWidget(self.txtBox_slot_id)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gBox_circuits = QtGui.QGroupBox(SlotWidget)
        self.gBox_circuits.setGeometry(QtCore.QRect(10, 40, 511, 101))
        self.gBox_circuits.setTitle(QtGui.QApplication.translate("SlotWidget", "Circuits", None, QtGui.QApplication.UnicodeUTF8))
        self.gBox_circuits.setFlat(False)
        self.gBox_circuits.setObjectName(_fromUtf8("gBox_circuits"))
        self.gridLayoutWidget = QtGui.QWidget(self.gBox_circuits)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.cboxes_layout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.cboxes_layout.setMargin(0)
        self.cboxes_layout.setObjectName(_fromUtf8("cboxes_layout"))

        self.retranslateUi(SlotWidget)
        QtCore.QMetaObject.connectSlotsByName(SlotWidget)

    def retranslateUi(self, SlotWidget):
        pass

