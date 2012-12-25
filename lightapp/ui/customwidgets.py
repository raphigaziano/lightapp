#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
customwidgets.py

Specialized widgets for the lightApp application

Author:  raphi <r.gaziano@gmail.com>
Created: 25/12/2012
Version: 1.0
'''
from PyQt4 import QtCore, QtGui

class ShowTableItem(QtGui.QTableWidgetItem):
    '''
    Specialized Table Item for easier handling from the main window.
    This is really not much more than a simple wrapper containing
    the whole objetc along with the base TableWidget attrs.
    '''
    def __init__(self, show):
        super(ShowTableItem, self).__init__(show.title)
        self.show = show
        self.setFlags(QtCore.Qt.ItemIsSelectable | 
                      QtCore.Qt.ItemIsEnabled)
