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
DEST_PATH   = SOURCE_PATH
PYUIC_PATH  = os.path.join('tools', 'pyuic4.bat')
PYRCC_PATH  = os.path.join('tools', 'pyrcc4.exe')

base_cmd = PYUIC_PATH + ' %s -o %s'
rc_cmd   = PYRCC_PATH + ' -py3 %s -o %s'

for f in os.listdir(SOURCE_PATH):
    if f.endswith('.qrc'): 
        cmd = rc_cmd % (
            os.path.join(SOURCE_PATH, f),
            os.path.join('.', f.replace('.qrc', '_rc.py'))
        )
    elif f.endswith('.ui'):
        cmd = base_cmd % (
            os.path.join(SOURCE_PATH, f),
            os.path.join(DEST_PATH, f.replace('.ui', '.py'))
        )
    else: continue
    print(cmd)
    os.system(cmd)
    
# Strip comments from ressource file 
# (An encoding error in there causes cx_freeze do fail):
print("cleaning ressources...")
import time
time.sleep(1)

lines = []
with open("ressources_rc.py", 'r') as f:
    lines = [l for l in f.readlines() if not l.startswith('#')]
with open("ressources_rc.py", 'w') as f:
    f.writelines(lines)

