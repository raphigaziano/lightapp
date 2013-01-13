'''
Temporary script to test html export function
'''
import os
print(os.getcwd())
from lightapp.fileio import xml, html

s = xml.load_show('popo.xml')
html.write_show(s, 'test.html')