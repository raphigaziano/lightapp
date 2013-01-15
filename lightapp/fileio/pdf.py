#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
pdf.py

File IO routines handling the pdf format.

Author:  raphi <r.gaziano@gmail.com>
Created: 07/01/2013
Version: 1.0
"""
from PyQt4 import QtGui
# @TODO: clean and solidify interface
def serialize_show(html):
    '''
    Create a QTextDocument from the received html.

    @param html: Source data. Should come from html.serialize_show().
    @returns:    A QTextDocument ready for printing.
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
