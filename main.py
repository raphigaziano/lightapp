#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

from lightapp import utils
from lightapp.ui import mainwin

if __name__=='__main__':
    app     = QtGui.QApplication(sys.argv)
    utils.init_logger()
    # move elswhere
    utils.show_dbgcons()
    utils.logger.info("Application intialized with arguments: %s" % 
        ", ".join(sys.argv))
    mainWin = mainwin.MainWindow()
    mainWin.show()
    app.exec_()
    utils.logger.info("done!")
