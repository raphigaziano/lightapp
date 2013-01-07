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

def get_date(s):
    '''
    Utility function converting either a python Date or a Qt QDate
    object to a timestamp for serialization.

    @param s: Date object, either from Qt or python's standard lib.
    @returns: Timestamp (float)
    '''
    try:
        return str(time.mktime(s.date.timetuple()))
    except AttributeError:
        date = s.date.toPyDate()
        return str(time.mktime(date.timetuple()))
    