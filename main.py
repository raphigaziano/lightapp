#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore
import sys

import config

from lightapp import show
from lightapp.ui import MainWindow
from lightapp.ui import customwidgets
 
class LightApp(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LightApp, self).__init__(parent)
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
        '''
        self.shows = []
        for s in show.load_shows(config.MASTER_SAVE_PATH):
            self.add_show(s)
 
    def connect_events(self): pass
 
    def main(self):
        self.show()
 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = LightApp()
    mainWin.main()
    app.exec_()
