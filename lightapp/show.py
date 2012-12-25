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
import xml.etree.ElementTree as ET
from PyQt4 import QtCore, QtGui

import config

XML_PATH = config.MASTER_SAVE_PATH
XML_TREE = ET.parse(XML_PATH)
XML_ROOT = XML_TREE.getroot()

class Show:
    '''
    Document class representing a single show and contains all of its
    different memory slots.
    It holds a serializer component able to generate either an xml or 
    csv representation of the entire show.
    '''
    def __init__(self):
        
        self.id_ = None
        self.title = ""
        self.num_slots = 0
        self.author = ""
        self.date = datetime.date.today()
        # Init xml/csv comps
        self.slots = []
        
    def load_base(self, node):
        '''Initialize the base show's data from the passed xml node'''
        self.id_        = int(node.get('id'))
        self.title      = node.find('title').text
        self.num_slots  = int(node.find('nbSlots').text)
        self.author     = node.find('auth').text
        d = datetime.date.fromtimestamp(float(node.find('date').text))
        self.date       = d


##########
# Factory

    
def load_shows():
    '''
    Generator function, instanciating show objects with their base info
    and yielding them to the caller.
    '''
    for s_node in XML_ROOT.iter('show'):
        s = Show()
        s.load_base(s_node)
        yield s
        
def save_base(show):
    '''
    '''
    print('Saving show...')
    
    # no id == new show
    if show.id_ is None:
        _save_base_new(show)
    else:
        _save_base_edited(show)
        
    XML_TREE.write(XML_PATH, encoding="UTF-8", 
                   xml_declaration=True)

def _save_base_new(s):
    '''
    '''
    s.id_ = _gen_id()
    new_s_elem = ET.SubElement(XML_ROOT, 'show', {'id': s.id_})

    title_elem = ET.SubElement(new_s_elem, 'title')
    title_elem.text = s.title
    slots_elem = ET.SubElement(new_s_elem, 'nbSlots')
    slots_elem.text = str(s.num_slots)
    auth_elem = ET.SubElement(new_s_elem, 'auth')
    auth_elem.text = s.author
    date_elem = ET.SubElement(new_s_elem, 'date')
    date_elem.text = _get_date(s)
    
def _save_base_edited(s):
    '''
    '''
    for s_node in XML_ROOT.iter('show'):
        if s_node.get('id') == str(s.id_):
            xml_elem = s_node
            break
    
    xml_elem.find('title').text = s.title
    xml_elem.find('nbSlots').text = str(s.num_slots)
    xml_elem.find('auth').text = s.author
    xml_elem.find('date').text = _get_date(s)
    
def _get_date(s):
    '''
    '''
    try:
        return str(time.mktime(s.date.timetuple()))
    except AttributeError:
        date = s.date.toPyDate()
        return str(time.mktime(date.timetuple()))
        
def _gen_id():
    '''
    '''
    max_id = 0
    for s in XML_ROOT.iter('show'):
        id_ = int(s.get('id'))
        if id_ > max_id: max_id = id_
    return str(max_id + 1)
