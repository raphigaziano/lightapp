#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

from lightapp import utils
from lightapp import show
from lightapp.ui import slotswin
from lightapp.ui import iomanager
from lightapp.ui.QDesigner import MainWindow as mainwin
 
class MainWindow(QtGui.QMainWindow, mainwin.Ui_MainWindow):
    '''
    Main application window.
    Responsible for editing a show's basic infos.
    The file IO routines are handled by a IOManager component.
    ''' #pylint: disable-msg=R0904
    def __init__(self, parent=None):
        utils.logger.info("Initializing main window...")
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self._show = None
        self.new_show()
        
        self.io = iomanager.IOManager(self)

        self.connect_events()
        utils.logger.info("MainWindow's ready")

    def new_show(self):
        '''Instantiate a new, blank show'''
        if self._show is not None and not self.io.prompt_for_save():
            return
        utils.logger.info("New show...")
        self._show = show.Show()
        utils.logger.debug("Instanciated %s" % self._show)
        self.fill_fields(self._show)
        self.connect_show_events()
        
    def enable_save(self):
        '''
        Enable the save and save_as actions and toggles the 
        window's modified flag on.
        '''
        self.action_save.setEnabled(True)
        self.action_save_as.setEnabled(True)

        self.setWindowModified(True)

    def disable_save(self):
        '''
        Disable the save and save_as actions and toggles the 
        window's modified flag off.
        '''
        self.action_save.setEnabled(False)
        self.action_save_as.setEnabled(False)
        
        self.setWindowModified(False)        
    
    def check_required_fields(self):
        '''
        Check if the required fields are filled.
        
        @returns True if all fields are ok, False otherwise.
        '''
        # @TODO: Check all fields except date
        if (#self.txtBox_show_title.text() == "" or
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
        s              = self._show    
        s.title        = self.txtBox_show_title.text()
        s.num_circuits = self.spinBox_show_nbSlots.value()
        s.author       = self.txtBox_show_author.text()
        s.date         = self.dateEdit_show_date.date()
        
    def fill_fields(self, s):
        '''
        Update the form's fields from the show's attrs

        @param s: source show object providing the fields' data
        '''
        self.txtBox_show_title.setText(s.title)
        self.spinBox_show_nbSlots.setValue(s.num_circuits)
        self.txtBox_show_author.setText(s.author)
        self.dateEdit_show_date.setDate(s.date)
    
    def edit_show_slots(self):
        '''Runs slot editing form'''
        if not self.check_required_fields():
            return
        self.update_show()
        utils.logger.info("Instanciating Editing Form...")
        d = slotswin.SlotsWindow(self._show)
        d.exec_()
        utils.logger.info("Mem slots editing complete.")

    ### QT Signals ###
    ##################
 
    def connect_events(self):
        '''Actions/Functions connections'''
        utils.logger.info("Basic file io events...")
        self.connect(self.action_new, QtCore.SIGNAL('triggered()'),
                     self.new_show)
        self.connect(self.action_open, QtCore.SIGNAL('triggered()'),
                     self.io.open_show)
        self.connect(self.action_save, QtCore.SIGNAL('triggered()'),
                     self.io.save_show)
        self.connect(self.action_save_as, QtCore.SIGNAL('triggered()'),
                     self.io.save_show_as)

        utils.logger.info("Export events...")
        self.connect(self.action_html, QtCore.SIGNAL('triggered()'),
                     self.io.export_html)
        ### @TODO: CSV ###
        self.connect(self.action_pdf, QtCore.SIGNAL('triggered()'),
                     self.io.export_pdf)
        ### TEST ###
        self.connect(self.action_print, QtCore.SIGNAL('triggered()'),
                     self.io.print_show)

        utils.logger.info("Editing event...")
        self.connect(self.btn_edit_slots, QtCore.SIGNAL('clicked()'),
                     self.edit_show_slots)

        utils.logger.info("DbgCons event...")
        self.connect(self.action_console, QtCore.SIGNAL('triggered()'),
                     utils.show_dbgcons)

        self.connect_show_events()
        
    def connect_show_events(self):
        '''
        Connect events emited by a show object to this window's
        slots.
        '''
        utils.logger.info("Show specific events...")
        self.connect(self.txtBox_show_title, 
                     QtCore.SIGNAL('textEdited(const QString&)'),
                     self._show.slot_modify)
        self.connect(self.spinBox_show_nbSlots, 
                     QtCore.SIGNAL('valueChanged(int)'),
                     self._show.slot_modify)
        self.connect(self.txtBox_show_author, 
                     QtCore.SIGNAL('textEdited(const QString&)'),
                     self._show.slot_modify)
        self.connect(self.dateEdit_show_date, 
                     QtCore.SIGNAL('dateChanged(const QDate&)'),
                     self._show.slot_modify)
                     
        self.connect(self._show, 
                     QtCore.SIGNAL('showModified()'),
                     self.enable_save)
        self.connect(self._show, 
                     QtCore.SIGNAL('showSaved()'),
                     self.disable_save)

    ### Events Overrides ###
    ########################
                     
    def dragEnterEvent(self, event): #pylint: disable-msg=R0201,C0103
        '''Drag & Drop Enter event'''
        if event.mimeData().hasUrls(): #hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event): #pylint: disable-msg=C0103
        '''Drag & Drop Drop event: load the dropped file'''
        for url in event.mimeData().urls():
            # the path returned has a weird slash before the drive 
            # letter, so get rid of it
            self.io.load_show(url.path()[1:])
            
    def closeEvent(self, event): #pylint: disable-msg=C0103
        '''Closing event: Prompt for saving if needed'''
        if self.io.prompt_for_save():
            # Ensure the whole application exits if this
            # window is closed.
            QtGui.QApplication.quit()
            event.accept()
        else:
            event.ignore()
