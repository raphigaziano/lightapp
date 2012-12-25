#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
show.py

Author:  raphi <r.gaziano@gmail.com>
Created: 25/12/2012
Version: 1.0
'''
from PyQt4 import QtCore, QtGui


class Show:
    '''
    Document class representing a single show and contains all of its
    different memory slots.
    It holds a serializer component able to generate either an xml or 
    csv representation of the entire show.
    '''
    def __init__(self, path=None):
        
        # Init xml/csv comps
        
        self.path = path
        self.title = path
        
    def load(self, path):
        ### DUMMY STUB ###
        pass

