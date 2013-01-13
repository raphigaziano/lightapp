#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
pdf.py

File IO routines handling the pdf format.

If any, the printing function will probably go there.

Author:  raphi <r.gaziano@gmail.com>
Created: 07/01/2013
Version: 1.0
"""
from PyQt4 import QtGui
# @TODO: clean and solidify interface
def serialize_show(html):
    '''
    '''
    doc = QtGui.QTextDocument()
    doc.setHtml(html)
    return doc

def _get_printer(fmt=None):
    '''
    '''
    printer = QtGui.QPrinter()
    printer.setFullPage(True)
    if fmt is not None:
        printer.setOutputFormat(fmt)
    return printer

def write_show(html, path):
    '''
    Careful: different interface from other mods!
    '''
    printer = _get_printer(QtGui.QPrinter.PdfFormat)
    printer.setOutputFileName(path)
    doc     = serialize_show(html)
    doc.print_(printer)
    # printer.newPage()

### TEST TEST TEST ###
def print_show(html):
    '''
    '''
    printer = _get_printer(QtGui.QPrinter.NativeFormat)
    dlg     = QtGui.QPrintDialog(printer)
    if dlg.exec_() == QtGui.QDialog.Accepted:
        doc     = serialize_show(html)
        painter = QtGui.QPainter()
        painter.begin(printer)
        # doc.print_(painter)
        doc.print_(printer)
        painter.end() # @TODO: TEST TEST TEST