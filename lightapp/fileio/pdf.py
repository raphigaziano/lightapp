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
<<<<<<< Updated upstream
# @TODO: clean and solidify interface
=======

>>>>>>> Stashed changes
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
    Instanciate a QPrinter object, sets it up and returns it.

    @param fmt: Optional printer format.
                Must be a valid QPrinter value.
    @return:    Qprinter object.
    '''
    printer = QtGui.QPrinter()
    printer.setFullPage(True)
    if fmt is not None:
        printer.setOutputFormat(fmt)
    return printer

def write_show(html, path):
    '''
    Write a show's data to a pdf file.

    @param html: Show's data, already formatted as html.
    @param path: File's path.
    '''
    printer = _get_printer(QtGui.QPrinter.PdfFormat)
    printer.setOutputFileName(path)
    doc     = serialize_show(html)
    doc.print_(printer)
    # printer.newPage()
