'''
Temporary script to test pdf export function
'''
from PyQt4 import QtGui
from lightapp.fileio import xml, html, pdf
#gnnn
import sys

s = xml.load_show('popo.xml')
html = html.serialize_show(s)

#gnnn
app = QtGui.QApplication(sys.argv)

pdf.write_show(html)

