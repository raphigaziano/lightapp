#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

from lightapp.ui import mainwin
 
def embed_ipython(w):
    ipshell = InteractiveShellEmbed(user_ns = dict(w = w))
    ipshell()

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = mainwin.MainWindow()
    mainWin.show()
    app.exec_()
