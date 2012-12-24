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

for f in os.listdir(SOURCE_PATH):
    cmd = 'python tools/pyuic.py ' + os.path.join(SOURCE_PATH, f) + \
        ' -o ' + os.path.join(DEST_PATH, f.replace('.ui', '.py'))
    print(cmd)
    os.system(cmd)
