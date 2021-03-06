#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
iomanager.py

Handles most of the dialog involved with files I/O.
The actual reading/writing of files is delegated to the fileio
package.

Author:  raphi <r.gaziano@gmail.com>
Created: 13/01/2013
Version: 1.0
"""
from PyQt4 import QtGui

from lightapp.fileio import xml, html, pdf, xlwt
from lightapp import utils

EXTS = {
    'XML' : "Xml Files (*.xml);;",
    'XLS' : "Excel Files (*.xls);;",
    'HTML': "Html Files (*.html);;",
    'PDF' : "Pdf Files (*.pdf);;",
    'ALL' : "All Files (*);;",
}

class IOManager():
    '''
    Holds a reference to its parent window, and handles most of the
    file dialogs.
    '''
    def __init__(self, parent):
        self.parent = parent
        self._show  = parent.show_ # shortcut

    ### Properties ###
    ##################

    @property
    def show(self):
        '''Simple Getter'''
        return self._show

    @show.setter
    def show(self, val):
        '''Update the parent window's show along with this one'''
        self.parent.show_ = self._show = val

    ### Common Dialogs ###
    ######################

    def _get_save_path(self, *exts):
        '''
        Url prompt before saving a file.

        @param exts: variable list of allowed extensions
        '''
        allowed_exts = "".join(
            [EXTS[e.upper()] for e in exts]
        )
        p = QtGui.QFileDialog.getSaveFileName(self.parent, 
                                              "Enregistrer sous:",
                                              '.', 
                                              allowed_exts
        )
        return p

    def _get_open_path(self, *exts):
        '''
        Url prompt for loading a file

        @param exts: variable list of allowed extensions
        '''
        allowed_exts = "".join(
            [EXTS[e.upper()] for e in exts]
        )
        p = QtGui.QFileDialog.getOpenFileName(self.parent, 
                                              "Ouvrir fichier:",
                                              '.', 
                                              allowed_exts
        )
        return p

    def prompt_for_save(self):
        '''
        Prompts the user to save if the current show has been
        updated.

        @returns True if we can go on (whether the show's saved or 
                 not), False otherwise.
        '''
        if not self.show.modified:
            return True
        msgBox = QtGui.QMessageBox
        choice = msgBox.warning(self.parent, 
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

    ### Basic(XML) IO ###
    #####################

    def save_show(self):
        '''
        Save the current show, prompting for url if needed

        @returns False if the save failed, True for success
        '''
        if not self.parent.check_required_fields():
            return False
        if self.show.path is None:
            return self.save_show_as()
        self.parent.update_show()
        xml.write_show(self.show)
        utils.logger.info("Show saved as %s"  % self.show.path)
        return True
        
    def save_show_as(self):
        '''Url prompt before saving the current show.'''
        p = self._get_save_path('xml', 'all')
        if p:
            self.show.path = p
            return self.save_show()

    def load_show(self, path, checked_save=False):
        '''Load the requested show'''
        if not checked_save and not self.prompt_for_save():
            return
        try:
            utils.logger.info("Loading show %s..." % path)
            self.show = xml.load_show(path)
        except Exception as e: # @FIXME Too general...
            utils.logger.exception("Error while loading file %s:"
                                    % path)
            QtGui.QMessageBox.critical(self.parent,
                                       "ONOES",
                                       "Impossible de lire ce fichier"
                                       "\n\n%s" % str(e)
            )
        else:
            self.parent.fill_fields(self.show)
            self.parent.connect_show_events()
            self.parent.disable_save()
            utils.logger.info("%s loaded" % path)
    
    def open_show(self):
        '''Url prompt for loading a show'''
        if not self.prompt_for_save():
            return
        p = self._get_open_path('xml', 'all')
        if p:
            return self.load_show(p, True)

    ### HTML IO ###
    ###############

    def export_html(self):
        '''Html Export Dialog'''
        p = self._get_save_path('html', 'all')
        if p: 
            html.write_show(self.show, p)
            utils.logger.info("Show exported as %s"  % p)

    ### Excel IO ###
    ################

    def export_xls(self):
        '''Excel Export Dialog'''
        p = self._get_save_path('xls', 'all')
        if p:
            try:
                xlwt.write_show(self.show, p)
                utils.logger.info("Show exported as %s"  % p)
            except IOError as e:
                QtGui.QMessageBox.critical(self.parent,
                                       "ONOES",
                                       "Impossible de d'écrire dans "
                                       "ce fichier!"
                                       "\n%s" % str(e) +
                                       "\n(Verifiez que le fichier "
                                        "n'est pas déjà ouvert, puis "
                                        "réessayez.)"
                )

    ### PDF IO ###
    ##############

    def export_pdf(self):
        '''Html Export Dialog'''
        shtml = html.serialize_show(self.show)
        p = self._get_save_path('pdf', 'all')
        if p: 
            pdf.write_show(shtml, p)
            utils.logger.info("Show exported as %s"  % p)

    ### Printing ###
    ################

    def print_show(self):
        '''Print dialog, followed by actual printing if validated'''
        printer = pdf._get_printer(QtGui.QPrinter.NativeFormat)
        dlg     = QtGui.QPrintDialog(printer)
        if dlg.exec_() == QtGui.QDialog.Accepted:
            shtml   = html.serialize_show(self.show)
            doc     = pdf.serialize_show(shtml)
            painter = QtGui.QPainter()
            painter.begin(printer)
            # doc.print_(painter)
            doc.print_(printer)
            painter.end() # @TODO: TEST TEST TEST
