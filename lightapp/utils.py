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
import logging.handlers
from lightapp.ui import qtdbg
DBG_CONS = None
logger   = None

def init_logger():
    '''
    Global logging intialization (should only be called at startup).
    Output redirected to a log file (full trace) & a custom 
    console-like widget (INFO level & above).
    '''
    global DBG_CONS, logger
    DBG_CONS = qtdbg.QDbgConsole()
    logger   = logging.getLogger('lightapp_log')
    logger.setLevel(logging.DEBUG)

    # create console handler, logs INFO leverl & above everthing.
    ch = logging.StreamHandler(DBG_CONS)
    ch.setLevel(logging.DEBUG)

    # create file handler which logs everything.
    fh = logging.handlers.TimedRotatingFileHandler('logs/log.txt',
                                                   when='midnight',
                                                   backupCount=10,
                                                   utc=True)
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
    '''Display the debug console.'''
    DBG_CONS.show()