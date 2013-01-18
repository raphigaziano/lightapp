#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

from lightapp import utils
from lightapp.ui import mainwin

# @TODO: Loading save with values not in the lists crashes
# @TODO: xls ugly if last slot is empty

if __name__=='__main__':
    app     = QtGui.QApplication(sys.argv)
    # Logger initialisation
    utils.init_logger()
    utils.logger.info("Application intialized with arguments: %s" % 
        ", ".join(sys.argv))
    # bigass try/catch
    try:
        mainWin = mainwin.MainWindow()
        mainWin.show()
        app.exec_()
    except Exception as e: 
        QtGui.QMessageBox.critical(mainWin,
                                   "ONOES!",
                                    "FATAL ERROR FTW"
                                    "\n\n%s" % str(e)
        )
        utils.logger.exception("!!!FATAL ERROR!!!")
        QtGui.QApplication.quit()
