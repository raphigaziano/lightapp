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

def write_show(html):
    '''
    '''
    printer = QtGui.QPrinter()
    printer.setOutputFileName("test.pdf")
    printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
    doc = serialize_show(html)
    doc.print(printer)
    printer.newPage()