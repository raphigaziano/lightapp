#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

from lightapp.ui.QDesigner import SlotsWindow
 
class SlotWindow(QtGui.QDialog, SlotsWindow.Ui_Dialog):
    '''
    '''
    def __init__(self, _show):
        super(SlotWindow, self).__init__()
        self.setupUi(self)
        
        self._show = _show
    
