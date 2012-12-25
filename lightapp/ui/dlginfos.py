#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import datetime
from PyQt4 import QtGui, QtCore

from lightapp.ui.QDesigner import DlgInfos
 
class DlgInfos(QtGui.QDialog, DlgInfos.Ui_dlg_show_infos):
    def __init__(self, parent=None, show=None):
        super(DlgInfos, self).__init__(parent)
        self.setupUi(self)
        
        self.s = show
        try:
            self.init_fields(self.s)
        except AttributeError: pass
            
    def init_fields(self, s):
        '''
        '''
        self.txtBox_show_title.setText(s.title)
        self.spinBox_show_nbSlots.setValue(s.num_slots)
        self.txtBox_show_author.setText(s.author)
        self.dateEdit_show_date.setDate(s.date)
        
    def update_show(self, s):
        '''
        '''
        # Only require title and a positive number of slots for now
        if (self.txtBox_show_title.text() == "" or
            self.spinBox_show_nbSlots.value() == 0):
            print("ERR MESSAGE!")
            return False
            
        s.title = self.txtBox_show_title.text()
        s.num_slots = self.spinBox_show_nbSlots.value()
        s.author = self.txtBox_show_author.text()
        s.date = self.dateEdit_show_date.date()
        return True

    def accept(self):
        if self.update_show(self.s):
            return super(DlgInfos, self).accept()
        return super(DlgInfos, self).reject()
