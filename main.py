#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
import sys

from lightapp.ui import mainWindow
 
class LightApp(QtGui.QMainWindow, win.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setupUi(self)
 
    def main(self):
        self.show()
 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = LightApp()
    mainWin.main()
    app.exec_()
