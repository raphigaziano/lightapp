#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
qtdbg.py

A simple PyQt output widget.
It's main use case is to serve as an output console, for debugging or 
other purposes.
It provides a file-like interface for ease of integration with other
python features such as the logging module, on top of a slightly 
pre-set QTextEdit widget.

Tested on:
    - Python 3.2, PyQt4, win7

@TODO: Verify the file-like api, and complete it if needed.

Author:  raphi <r.gaziano@gmail.com>
Created: 08/01/2013
Version: 1.0
"""
from PyQt4 import QtGui, QtCore

WIDTH  = 320
HEIGHT = 320

class QDbgConsole(QtGui.QTextEdit):
    '''
    A simple QTextEdit, with a few pre-set attributes and a file-like
    interface.
    '''
    def __init__(self, parent=None, w=WIDTH, h=HEIGHT):
        super(QDbgConsole, self).__init__(parent)
        
        self.setFixedSize(w, h)  # @FIXME: Not fixed size
        self.setReadOnly(True)

    ### File-like interface ###
    ###########################

    def read(self, size=None):
        '''
        Returns size bytes from the console's current text, or the 
        whole text if no size is specified.
        '''
        if size is None:
            return self.toPlainText()
        return self.toPlainText()[:size]

    def readLine(self, size=None):
        '''
        Stub method. Not sure of the exact requirement.
        '''
        raise NotImplementedError()

    def write(self, msg):
        '''Add msg to the console's output, on a new line.'''
        self.append(msg)

    def close(self):
        '''Stub method, does nothing.'''
        pass


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w   = QDbgConsole()
    w.show()

    ### Quick Testing ###
    ##################### 

    for _ in range(100):
        w.write("TestMessage, yay \\o/")
    print("====================")
    print(w.read())
    print("====================")
    s = w.read(100)
    assert(len(s) == 100)
    print(s)
    print("====================")

    app.exec_()
