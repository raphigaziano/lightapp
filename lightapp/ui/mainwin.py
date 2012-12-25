#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

import config

from lightapp import show
from lightapp.ui import customwidgets
from lightapp.ui import dlginfos
from lightapp.ui.QDesigner import MainWindow
 
class MainWindow(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.table_shows.setColumnWidth(0, 260)
        self.table_shows.setColumnWidth(1, 50)
        self.table_shows.setColumnWidth(2, 50)
        
        self.load_shows()
        
        self.connect_events()
        
    def add_show(self, show):
        '''Add a single show to the list and table'''
        self.shows.append(show)
        i = len(self.shows) -1 #ismellabug
        self.table_shows.insertRow(i)
        
        newitem = customwidgets.ShowTableItem(show)
        self.table_shows.setItem(i, 0, newitem)
        
        btn_infos = QtGui.QPushButton(self.table_shows)
        btn_infos.setText('Infos')
        self.connect(btn_infos, QtCore.SIGNAL("clicked()"), 
                     self.edit_show_infos)
        btn_edit  = QtGui.QPushButton(self.table_shows)
        btn_edit.setText('Edit')
        self.connect(btn_edit, QtCore.SIGNAL("clicked()"), 
                     self.edit_show_slots)
                     
        self.table_shows.setCellWidget(i, 1, btn_infos)
        self.table_shows.setCellWidget(i, 2, btn_edit)
        
    def selected_show(self):
        cur_row = self.table_shows.currentRow()
        return self.table_shows.item(cur_row, 0).show
        
    def new_show(self): 
        '''
        '''
        new_s = show.Show()
        d = dlginfos.DlgInfos(show=new_s)
        # Is this robust enough ?
        if d.exec_():
            show.save_base(new_s)
            self.add_show(new_s)
        
    def edit_show_infos(self):
        '''
        '''
        s = self.selected_show()
        d = dlginfos.DlgInfos(show=s)
        if d.exec_():
            show.save_base(s)
            
    
    def edit_show_slots(self):
        '''
        '''
        print("edit slots")
        
    def load_shows(self):
        '''
        Load every saved show with their basic data.
        Called mainly on startup.
        '''
        self.shows = []
        for s in show.load_shows():
            self.add_show(s)
 
    def connect_events(self):
        '''
        '''
        self.connect(self.btn_new, QtCore.SIGNAL("clicked()"), 
                     self.new_show)
        ### other buttons...
        self.table_shows.itemDoubleClicked.connect(self.edit_show_infos)
 
    def main(self):
        self.show()
