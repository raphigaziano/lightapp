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
    def __init__(self, id_, num_circuits, parent_slot):
        
        self.id_ = id_
        self.in_ = ""
        self.out = ""
        
        self.num_circuits = num_circuits
        self.circuits = {i: 0 for i in range(num_circuits)}

        self.parent_slot = parent_slot
    
      
def load_slot(s_elem, slot):
    ''' '''
    s = MemSlot(s_elem.get('id'), slot.num_circuits, slot)
    s.in_ = s_elem.get('in')
    s.out = s_elem.get('out')
    # Circuits
    for c_elem in s_elem.iter("circuit"):
        s.circuits[int(c_elem.get('i'))] = c_elem.get('val')
    return s
        
def save_slot(s):
    ''' '''
    s_elem = ET.Element('slot')
    s_attrs = s_elem.attrib
    s_attrs.setdefault("id", str(s.id_))
    s_attrs.setdefault("in", str(s.in_))
    s_attrs.setdefault("out", str(s.out))
    # Circuits
    circs_elem = ET.SubElement(s_elem, "circuits")
    for i, v in s.circuits.items():
        c_elem = ET.SubElement(circs_elem, "circuit")
        c_elem.attrib = dict(i=str(i), val=str(v))
    
    return s_elem
