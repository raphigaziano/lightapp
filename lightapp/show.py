#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
show.py

Author:  raphi <r.gaziano@gmail.com>
Created: 25/12/2012
Version: 1.0
'''
import datetime
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    
from PyQt4 import QtCore

from lightapp import memslot
from lightapp import utils

class Show(QtCore.QObject): #pylint: disable-msg=R0902
    '''
    Document class representing a single show and containing all of
    its different memory slots.
    Inherits QObject to be able to emit signals.
    '''
    def __init__(self):
        super(Show, self).__init__()
        self.title        = ""
        self.num_circuits = 0
        self.author       = ""
        self.date         = datetime.date.today()
        
        self.path = None

        self.slots = []
        
        self._modified = False
        
    def add_slot(self):
        '''
        Add a new memory slot.

        @returns the new mem slot.
        '''
        i = int(self.slots[-1].id_) + 1 if self.slots else 1
        s = memslot.MemSlot(i, self)
        self.slots.append(s)
        return s

    def remove_slot(self, slot):
        '''
        Supress a memory slot.

        @param slot: the slot object to remove.
        '''
        print("Supressing memslot %s" % repr(slot))
        self.slots.remove(slot)
        
    def load_base(self, node):
        '''
        Initialize the base show's data.

        @param node: Xml node containing the show's base infos.
        '''
        self.title          = node.find('title').text
        self.num_circuits   = int(node.find('nbCircuits').text)
        self.author         = node.find('auth').text
        d = datetime.date.fromtimestamp(float(node.find('date').text))
        self.date = d
            
    ### Properties ###
    
    @property
    def modified(self):
        '''Simple setter'''
        return self._modified
    
    @modified.setter
    def modified(self, val):
        '''
        Emits an appropriate signal everytime the _modified flag is
        changed.
        '''
        self._modified = val
        if self._modified:
            self.emit(QtCore.SIGNAL('showModified()'))
        else:
            self.emit(QtCore.SIGNAL('showSaved()'))

    def slot_modify(self):
        '''
        Qt Slot.
        Sets the _modified flag to true if it wasn't already.
        '''
        print("show modified")
        if not self.modified: 
            self.modified = True
