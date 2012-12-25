#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
updateGui.py

Shorthand script to generate a new python class from any changed/new
ui file created from QtDesigner.

Author:  raphi <r.gaziano@gmail.com>
Created: 24/12/2012
Version: 1.0
'''
import os

SOURCE_PATH = os.path.join('lightapp', 'ui', 'QDesigner')
DEST_PATH   = os.path.join('lightapp', 'ui')
PYUIC_PATH  = os.path.join('tools', 'pyuic.py')

base_cmd = 'python ' + PYUIC_PATH + ' %s -o %s'

for f in os.listdir(SOURCE_PATH):
    cmd = base_cmd % (os.path.join(SOURCE_PATH, f),
                      os.path.join(DEST_PATH, f.replace('.ui', '.py')))
    print(cmd)
    os.system(cmd)
