#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
show.py

Author:  raphi <r.gaziano@gmail.com>
Created: 25/12/2012
Version: 1.0
'''
import datetime
import time
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    
from PyQt4 import QtCore

from lightapp import memslot

class Show(QtCore.QObject):
    '''
    Document class representing a single show and containing all of
    its different memory slots.
    Inherits QObject to be able to emit signals.
    '''
    def __init__(self):
        super(Show, self).__init__()
        self.title = ""
        self.num_circuits = 0
        self.author = ""
        self.date = datetime.date.today()
        
        self.path = None

        self.slots = []
        
        self._modified = False
        
    def add_slot(self):
        '''
        Add a new memory slot.

        @returns the new mem slot.
        '''
        i = int(self.slots[-1].id_) + 1 if self.slots else 1
        s = memslot.MemSlot(i, self.num_circuits, self)
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

##########
# Factory

def load_show(p):
    '''
    Instanciates a new show from a saved Xml file.

    @param p: path to the Xml file.
    @returns the new show object.
    '''
    tree = ET.parse(p)
    root = tree.getroot()
    
    s = Show()
    s.path = p
    base = root.find('baseInfos')
    s.load_base(base)
    
    # slots
    for slot_elem in root.iter('slot'):
        s.slots.append(memslot.load_slot(slot_elem, s))
    
    return s
    
    
def save_show(s):
    '''
    Serialize a show object and save it to an Xml file.

    @param s: show to serialize & save.
    '''
    print("Saving show...")
    root = ET.Element('show')
    
    base = ET.SubElement(root, 'baseInfos')
    title_elem = ET.SubElement(base, 'title')
    title_elem.text = s.title
    slots_elem = ET.SubElement(base, 'nbCircuits')
    slots_elem.text = str(s.num_circuits)
    auth_elem = ET.SubElement(base, 'auth')
    auth_elem.text = s.author
    date_elem = ET.SubElement(base, 'date')
    date_elem.text = _get_date(s)
    
    # slots
    mem_elem = ET.SubElement(root, 'memSlots')
    for slot in s.slots:
        mem_elem.append(memslot.save_slot(slot))
    
    tree = ET.ElementTree(root)
    tree.write(s.path, encoding='UTF-8', xml_declaration=True)
    
    s.modified = False
    
#######
# Utils
# (Should probably be moved)

def _get_date(s):
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
    