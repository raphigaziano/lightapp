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
        # Setting date first to avoid raising an exception too soon
        try:
            self.dateEdit_show_date.setDate(s.date)
        except AttributeError:
            self.dateEdit_show_date.setDate(datetime.date.today())
        self.txtBox_show_title.setText(s.title)
        self.spinBox_show_nbSlots.setValue(s.num_slots)
        self.txtBox_show_author.setText(s.author)

    def accept(self):
        print("UPDATESHOWOBJ")
        return super(DlgInfos, self).accept()

    def reject(self):
        return super(DlgInfos, self).reject()
