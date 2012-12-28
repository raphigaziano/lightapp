#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

from lightapp import show
from lightapp.ui import slotswin
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
        if hasattr(self, '_show') and not self.prompt_for_save():
            return
        self._show = show.Show()
        self._fill_fields(self._show)
        self._connect_show_events()
        
    def save_show(self):
        '''Save the current show, prompting for url if needed'''
        if not self._check_required_fields():
            return False
        if self._show.path is None:
            return self.save_show_as()
        self.update_show()
        show.save_show(self._show)
        return True
        
    def save_show_as(self):
        '''Url prompt before saving the current show.'''
        p = QtGui.QFileDialog.getSaveFileName(self, 
                                              "Enregistrer sous:",
                                              '.', 
                                              "Xml Files (*.xml);;"
                                              "All Files (*);;"
        )
        if p:
            self._show.path = p
            return self.save_show()
    
    def prompt_for_save(self):
        ''' '''
        # NEEDZ TEST & WORK #
        if not self._show._modified:
            return True
        msgBox = QtGui.QMessageBox
        choice = msgBox.warning(self, 
                                "Fichier pas frais!",
                                "Des modifications ont été apportées.\n"
                                "Voulez vous sauvegarder ces "
                                "changements?",
                                msgBox.Yes | msgBox.No | msgBox.Cancel,
                                msgBox.Yes)
        if choice == msgBox.Yes:
            return self.save_show()
        elif choice == msgBox.Cancel: 
            return False
        return True
        
    def enable_save(self):
        ''' '''
        self.action_save.setEnabled(True)
        self.action_save_as.setEnabled(True)

        self.setWindowModified(True)

    def disable_save(self):
        ''' '''
        self.action_save.setEnabled(False)
        self.action_save_as.setEnabled(False)
        
        self.setWindowModified(False)
    
    def load_show(self, path, checked_save=False):
        '''Load the requested show'''
        if checked_save and not self.prompt_for_save():
            return
        try:
            self._show = show.load_show(path)
            self._fill_fields(self._show)
            self._connect_show_events()
        except Exception as e: # Too general...
            QtGui.QMessageBox.critical(self,
                                       "ONOES",
                                       "Impossible de lire ce fichier"
                                       "\n\n%s" % (str(e))
            )
    
    def open_show(self):
        '''Url prompt for loading a show'''
        if not self.prompt_for_save():
            return
        p = QtGui.QFileDialog.getOpenFileName(self, 
                                              "Ouvrir fichier:",
                                              '.', 
                                              "Xml Files (*.xml);;"
                                              "All Files (*);;"
        )
        if p:
            return self.load_show(p, True)
        
    
    def _check_required_fields(self):
        '''
        Check if the required fields are filled.
        Only require the title and circuit number for now.
        '''
        if (self.txtBox_show_title.text() == "" or
            self.spinBox_show_nbSlots.value() == 0):
            QtGui.QMessageBox.critical(self,
                                       "ONOES",
                                       "Le nom du spectacle et le "
                                       "nombre de circuits doivent être"
                                       " renseignés."
            )
            return False
        return True
    
    def update_show(self):
        '''
        Update the show object from the form's fields.
        Mainly useful before saving.
        '''
        s = self._show    
        s.title = self.txtBox_show_title.text()
        s.num_circuits = self.spinBox_show_nbSlots.value()
        s.author = self.txtBox_show_author.text()
        s.date = self.dateEdit_show_date.date()
        
    def _fill_fields(self, s):
        '''Update the form's fields from the show's attrs'''
        self.txtBox_show_title.setText(s.title)
        self.spinBox_show_nbSlots.setValue(s.num_circuits)
        self.txtBox_show_author.setText(s.author)
        self.dateEdit_show_date.setDate(s.date)
    
    def edit_show_slots(self):
        '''Runs slot editing form'''
        if not self._check_required_fields():
            return
        self.update_show()
        d = slotswin.SlotWindow(self._show)
        ret = d.exec_()
        print(ret)
        
    ### Events ###
 
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
        # Edit button
        self.connect(self.btn_edit_slots, QtCore.SIGNAL('clicked()'),
                     self.edit_show_slots)
        
        self._connect_show_events()
        
    def _connect_show_events(self):
        ''' '''
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
                     
        self.connect(self._show, 
                     QtCore.SIGNAL('showModified()'),
                     self.enable_save)
        self.connect(self._show, 
                     QtCore.SIGNAL('showSaved()'),
                     self.disable_save)
                     
    def dragEnterEvent(self, event):
        '''Drag & Drop Enter event'''
        if not event.mimeData().hasUrls(): #hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        '''Drag & Drop Drop event: load the dropped file'''
        for url in event.mimeData().urls():
            # the path returned has a weird slash before the drive 
            # letter, so get rid of it
            self.load_show(url.path()[1:])
            
    def closeEvent(self, event):
        if self.prompt_for_save():
            event.accept()
        else:
            event.ignore()
