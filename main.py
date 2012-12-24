#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
import sys

from lightapp.ui import MainWindow
 
class LightApp(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LightApp, self).__init__(parent)
        self.setupUi(self)
 
    def main(self):
        self.show()
 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = LightApp()
    mainWin.main()
    app.exec_()
