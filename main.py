#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

from lightapp import utils
from lightapp.ui import mainwin

if __name__=='__main__':
    app     = QtGui.QApplication(sys.argv)
    utils.init_logger()
    utils.logger.info("Application intialized with arguments: %s" % 
        ", ".join(sys.argv))
    # bigass try
    mainWin = mainwin.MainWindow()
    mainWin.show()
    app.exec_()
    # bigass catch: 
    #   err mess, dump log, exit
    # make sur dbgcons closes
    utils.logger.info("done!")
