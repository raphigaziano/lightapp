#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
show.py

Author:  raphi <r.gaziano@gmail.com>
Created: 25/12/2012
Version: 1.0
'''
import datetime
from PyQt4 import QtCore, QtGui

class Show:
    '''
    Document class representing a single show and contains all of its
    different memory slots.
    It holds a serializer component able to generate either an xml or 
    csv representation of the entire show.
    '''
    def __init__(self):
        
        # Init xml/csv comps
        self.slots = []
        
    def load_base(self, node):
        '''Initialize the base show's data from the passed xml node'''
        self.title      = node.find('title').text
        self.num_slots  = int(node.find('nbSlots').text)
        self.author     = node.find('auth').text
        d = datetime.date.fromtimestamp(float(node.find('date').text))
        self.date       = d


##########
# Factory

import xml.etree.ElementTree as ET

    
def load_shows(xml_path):
    '''
    Generator function, instanciating show objects with their base info
    and yielding them to the caller.
    '''
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for s_node in root.iter('show'):
        s = Show()
        s.load_base(s_node)
        yield s
        
