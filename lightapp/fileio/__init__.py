#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
fileio.__init__.py

Package containing the different modules handling the reading
and writing of a show's data to disk.

Each module is responsible for a different file format and will 
provide at least a serialize_showand a write_show functions.
A lower level save_slot(s) function will also be provided, but 
shouln't be called directly in most cases (the higher level functions
will take care of it).
Some of the modules wil also provide load_show/load_slot(s) functions
to read data from file (currently only the xml one does that).
"""

from . import xml
from . import html
from . import xlwt
from . import pdf
