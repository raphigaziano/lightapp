#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
fileio.__init__.py

Package containing the different modules handling the reading
and writing of a show's data to disk.

Each module is responsible for a different file format and will 
provide at least a save_show and save_slot(s) function (The higher
level save_show will take care of calling save_slot in most cases).
Some of the modules wil also provide load_show/load_slot(s) functions
to read data from file (currently only the xml one does that).
"""

from lightapp.fileio import xml
from lightapp.fileio import html
from lightapp.fileio import xlwt
from lightapp.fileio import pdf