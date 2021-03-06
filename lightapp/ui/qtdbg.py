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
Since it inherits QTextEdit directly, all of the widget's methods are
available directly for further customization or GUI integration.

Tested on:
    - Python 3.2, PyQt4, win7

Author:  raphi <r.gaziano@gmail.com>
Created: 08/01/2013
Version: 1.0
"""
from io import StringIO
from PyQt4 import QtGui

class QDbgConsole(QtGui.QTextEdit):
    '''
    A simple QTextEdit, with a few pre-set attributes and a file-like
    interface.
    '''
    # Feel free to adjust those
    WIDTH  = 480
    HEIGHT = 320
    
    def __init__(self, parent=None, w=WIDTH, h=HEIGHT):
        super(QDbgConsole, self).__init__(parent)
        
        self._buffer = StringIO()

        self.resize(w, h)
        self.setReadOnly(True)

    ### File-like interface ###
    ###########################

    def write(self, msg):
        '''Add msg to the console's output, on a new line.'''
        self.insertPlainText(msg)
        # Autoscroll
        self.moveCursor(QtGui.QTextCursor.End)
        self._buffer.write(msg)

    # Most of the file API is provided by the contained StringIO 
    # buffer.
    # You can redefine any of those methods here if needed.

    def __getattr__(self, attr):
        '''
        Fall back to the buffer object if an attribute can't be found.
        '''
        return getattr(self._buffer, attr)


# -- Testing
if __name__ == '__main__':

    import sys
    
    app = QtGui.QApplication(sys.argv)
    widget   = QDbgConsole()
    widget.show()

    for _ in range(100):
        widget.write("TestMessage, yay \\o/")
    print("====================")
    print(widget.read())
    print("====================")
    widget.seek(0)
    s = widget.read(100)
    assert(len(s) == 100)
    print(s)
    print("====================")

    app.exec_()
