#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
memslot.py

Author:  raphi <r.gaziano@gmail.com>
Created: 26/12/2012
Version: 1.0
'''
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

NUM_CIRC_BY_LINE = 6

class MemSlot:
    '''
    '''
    def __init__(self, num_circuits):
        
        self.id_ = ""
        self.in_ = ""
        self.out = ""
        
        self.num_circuits = num_circuits
        self.circuits = {i: 0 for i in range(num_circuits)}
      
    
      
def load_slot(s_elem, num_circs):
    ''' '''
    s = MemSlot(num_circs)
    s.id_ = s_elem.get('id')
    s.in_ = s_elem.get('in')
    s.out = s_elem.get('out')
    
    # Get circuit vals
        
def save_slot(s):
    ''' '''
    s_elem = ET.Element('slot')
    s_attrs = s_elem.attrib
    s_attrs.setdefault("id", s.id_)
    s_attrs.setdefault("in", s.in_)
    s_attrs.setdefault("out", s.out)
    
    circs_elem = ET.SubElement(s_elem, "circuits")
    for i, v in s.circuits.items():
        c_elem = ET.SubElement(circs_elem, "circuit")
        # write circs values...
    
    return s_elem
