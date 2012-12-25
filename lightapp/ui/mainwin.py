#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

import config

from lightapp import show
from lightapp.ui import customwidgets
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
        i = len(self.shows) -1
        self.table_shows.insertRow(i)
        
        newitem = customwidgets.ShowTableItem(show)
        self.table_shows.setItem(i, 0, newitem)
        
        btn_infos = QtGui.QPushButton(self.table_shows)
        btn_infos.setText('Infos')
        btn_edit  = QtGui.QPushButton(self.table_shows)
        btn_edit.setText('Edit')
        
        self.table_shows.setCellWidget(i, 1, btn_infos)
        self.table_shows.setCellWidget(i, 2, btn_edit)

        
    def load_shows(self):
        '''
        Load every saved show with their basic data.
        Called mainly on startup.
        '''
        self.shows = []
        for s in show.load_shows(config.MASTER_SAVE_PATH):
            self.add_show(s)
 
    def connect_events(self): pass
 
    def main(self):
        self.show()
