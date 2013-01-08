#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
utils.py

Set of utility functions needed around the soft

Author:  raphi <r.gaziano@gmail.com>
Created: 07/01/2013
Version: 1.0
"""
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
    @returns: Fomatted date string
    '''
    return d.strftime(f)