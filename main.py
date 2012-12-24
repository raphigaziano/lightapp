#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
import sys

from lightapp.ui import MainWindow
 
class LightApp(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LightApp, self).__init__(parent)
        self.setupUi(self)
        
        ### TESTING ###
        for i in range(5):
            self.tableWidget.insertRow(i)
            #~ self.tableWidget.setItem(i, 1, 'popo')
            #~ self.tableWidget.setItem(i, 1, 'papa')
 
    def main(self):
        self.show()
 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = LightApp()
    mainWin.main()
    app.exec_()
