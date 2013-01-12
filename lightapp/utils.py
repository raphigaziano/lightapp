#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
utils.py

Set of utility functions needed around the soft

Author:  raphi <r.gaziano@gmail.com>
Created: 07/01/2013
Version: 1.0
"""

### Date utilities ###
######################

import time

TIME_FORMAT = "%d/%m/%Y"

def get_timestamp(d):
    '''
    Utility function converting either a python Date or a Qt QDate
    object to a timestamp for serialization.

    @param d: Date object, either from Qt or python's standard lib.
    @returns: Timestamp (float)
    '''
    try:
        return str(time.mktime(d.timetuple()))
    except AttributeError:
        date = d.toPyDate()
        return str(time.mktime(date.timetuple()))
    
def get_datestr(d, f=TIME_FORMAT):
    '''
    Utility function returning a python Date or Qt QDate object 
    as a formatted string.

    @param d: Date object, either from Qt or python's standard lib.
    @param f: Format string. defaults to the local constant 
              TIME_FORMAT, ie dd/mm/yyyy
    @returns: Fomatted date string
    '''
    try:
        return d.strftime(f)
    except AttributeError:
        return d.toPyDate().strftime(f)

### Logging ###
###############

import logging
from lightapp.ui import qtdbg
DBG_CONS = None
logger = None

def init_logger():
    ''' '''
    global DBG_CONS, logger
    DBG_CONS = qtdbg.QDbgConsole()
    logger = logging.getLogger('lightapp_log')
    logger.setLevel(logging.DEBUG)

    # create console handler, logs everthing.
    ch = logging.StreamHandler(DBG_CONS)
    ch.setLevel(logging.INFO)

    # create file handler which only warnings and worse.
    fh = logging.FileHandler('logs/log')
    fh.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - '
                                  '%(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

def show_dbgcons():
    ''' '''
    DBG_CONS.show()