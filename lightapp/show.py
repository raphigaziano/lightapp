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


class Show(QtCore.QObject):
    '''
    Document class representing a single show and contains all of its
    different memory slots.
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
        
    def load_base(self, node):
        '''Initialize the base show's data from the passed xml node'''
        self.title      = node.find('title').text
        self.num_circuits  = int(node.find('nbCircuits').text)
        self.author     = node.find('auth').text
        d = datetime.date.fromtimestamp(float(node.find('date').text))
        self.date       = d
            
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

    def modify(self):
        '''
        Convenience method: needed to connect Qt signals
        (those can't set an attribute directly and need a callable).
        '''
        if not self.modified: 
            self.modified = True

##########
# Factory

def load_show(p):
    '''
    '''
    tree = ET.parse(p)
    root = tree.getroot()
    
    s = Show()
    s.path = p
    base = root.find('baseInfos')
    s.load_base(base)
    
    # slots....
    
    return s
    
    
def save_show(s):
    '''
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
    
    # slots...
    
    tree = ET.ElementTree(root)
    tree.write(s.path, encoding='UTF-8', xml_declaration=True)
    
    s.modified = False
    
    
def _get_date(s):
    '''
    '''
    try:
        return str(time.mktime(s.date.timetuple()))
    except AttributeError:
        date = s.date.toPyDate()
        return str(time.mktime(date.timetuple()))
    
    
# IGNORE
########
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
    
        
