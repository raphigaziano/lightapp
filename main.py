#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

from lightapp.ui import mainwin

if __name__=='__main__':
    app     = QtGui.QApplication(sys.argv)
    mainWin = mainwin.MainWindow()
    mainWin.show()
    app.exec_()
    print("done!")
