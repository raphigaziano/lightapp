#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

import config

from lightapp import show
from lightapp.ui.QDesigner import MainWindow
 
class MainWindow(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    '''
    Main application window.
    Responsible for handling the file IO routines and editing a 
    show's basic infos. 
    '''
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.new_show()
        
        self.connect_events()
        
    def new_show(self):
        '''Instantiate a new, blank show'''
        self._show = show.Show()
        self._fill_fields(self._show)
        
    def save_show(self):
        '''Save the current show, prompting for url if needed'''
        if not self.update_show():  return
        if self._show.path is None: return self.save_show_as()
        show.save_show(self._show)
        
    def save_show_as(self):
        '''Url prompt before saving the current show.'''
        p = QtGui.QFileDialog.getSaveFileName(self, 
                                              "Ouvrir fichier:",
                                              '.', 
                                              "Xml Files (*.xml);;"
                                              "All Files (*);;"
        )
        if p:
            self._show.path = p
            return self.save_show()
        
    
    def load_show(self, path):
        '''Load the requested show'''
        try:
            self._show = show.load_show(path)
            self._fill_fields(self._show)
        except: # Too general...
            print("ERR MESSAGE!")
    
    def open_show(self):
        '''Url prompt for loading a show'''
        print("CHECK FOR SAVE!!!")
        p = QtGui.QFileDialog.getOpenFileName(self, 
                                              "Ouvrir fichier:",
                                              '.', 
                                              "Xml Files (*.xml);;"
                                              "All Files (*);;"
        )
        if p:
            return self.load_show(p)
        
        
    def update_show(self):
        '''
        Update the show object from the form's fields.
        Mainly useful before saving.
        '''
        # Only require title and a positive number of slots for now
        # MOVEOUT!!!
        if (self.txtBox_show_title.text() == "" or
            self.spinBox_show_nbSlots.value() == 0):
            print("ERR MESSAGE!")
            return False
        s = self._show    
        s.title = self.txtBox_show_title.text()
        s.num_slots = self.spinBox_show_nbSlots.value()
        s.author = self.txtBox_show_author.text()
        s.date = self.dateEdit_show_date.date()
        return True
        
    def _fill_fields(self, s):
        '''Update the form's fields from the show's attrs'''
        self.txtBox_show_title.setText(s.title)
        self.spinBox_show_nbSlots.setValue(s.num_slots)
        self.txtBox_show_author.setText(s.author)
        self.dateEdit_show_date.setDate(s.date)
    
    def edit_show_slots(self):
        '''Runs slot editing form'''
        print("edit slots")
 
    def connect_events(self):
        '''Actions/Functions connections'''
        # IO Actions
        self.connect(self.action_new, QtCore.SIGNAL('triggered()'),
                     self.new_show)
        self.connect(self.action_open, QtCore.SIGNAL('triggered()'),
                     self.open_show)
        self.connect(self.action_save, QtCore.SIGNAL('triggered()'),
                     self.save_show)
        self.connect(self.action_save_as, QtCore.SIGNAL('triggered()'),
                     self.save_show_as)
        # Show modifying events
        self.connect(self.txtBox_show_title, 
                     QtCore.SIGNAL('textEdited(const QString&)'),
                     self._show.modify)
        self.connect(self.spinBox_show_nbSlots, 
                     QtCore.SIGNAL('valueChanged(int)'),
                     self._show.modify)
        self.connect(self.txtBox_show_author, 
                     QtCore.SIGNAL('textEdited(const QString&)'),
                     self._show.modify)
        self.connect(self.dateEdit_show_date, 
                     QtCore.SIGNAL('dateChanged(const QDate&)'),
                     self._show.modify)
                     
    def dragEnterEvent(self, event):
        '''Drag & Drop Enter event'''
        if event.mimeData().hasUrls(): #hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        '''Drag & Drop Drop event: load the dropped file'''
        for url in event.mimeData().urls():
            # the path returned has a weird slash before the drive 
            # letter, so get rid of it
            self.load_show(url.path()[1:])
