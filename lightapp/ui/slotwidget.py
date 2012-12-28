#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

from lightapp.ui.QDesigner import SlotWidget
 
class SlotWidget(QtGui.QWidget, SlotWidget.Ui_SlotWidget):
    '''
    '''
    def __init__(self, parent=None, slot=None):
        super(SlotWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.slot = slot
