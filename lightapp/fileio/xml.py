#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
xml.py

File IO routines handling the Xml format.

Author:  raphi <r.gaziano@gmail.com>
Created: 07/01/2013
Version: 1.0
"""
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from lightapp import utils
from lightapp.show import Show
from lightapp.memslot import MemSlot

def load_show(p):
    '''
    Instanciates a new show from a saved Xml file.

    @param p: path to the Xml file.
    @returns: the new show object.
    '''
    tree = ET.parse(p)
    root = tree.getroot()
    
    s      = Show()
    s.path = p
    base   = root.find('baseInfos')
    s.load_base(base)
    
    # slots
    for slot_elem in root.iter('slot'):
        s.slots.append(load_slot(slot_elem, s))
    
    return s
    
    
def serialize_show(s):
    '''
    Serialize a show object as en Xml Tree.

    @param s: show to serialize & save.
    @returns: Xml Tree representing the show's data
    '''
    print("Saving show...")
    root = ET.Element('show')
    
    base            = ET.SubElement(root, 'baseInfos')
    title_elem      = ET.SubElement(base, 'title')
    title_elem.text = s.title
    slots_elem      = ET.SubElement(base, 'nbCircuits')
    slots_elem.text = str(s.num_circuits)
    auth_elem       = ET.SubElement(base, 'auth')
    auth_elem.text  = s.author
    date_elem       = ET.SubElement(base, 'date')
    date_elem.text  = utils.get_timestamp(s.date)
    
    # slots
    mem_elem = ET.SubElement(root, 'memSlots')
    for slot in s.slots:
        mem_elem.append(save_slot(slot))
    
    s.modified = False
    tree = ET.ElementTree(root)
    return tree

def write_show(s, p=""):
    '''
    Write a show's data to an xml file.

    @param s: Show data. Can be either a show object or an already
              serialized Xml tree.
    @param p: Optional path, in case we're dealing with an already
              serialized tree (which won't contain any path info).
              If needed but not provided, the file will be written
              in the cwd and its name will default to the show's 
              title.
    '''
    if isinstance(s, Show):
        path = s.path
        tree = serialize_show(s)
    elif isinstance(s, ET.ElementTree):
        path = p or "%s%s.xml" % (p, s.title)
        tree = s
    tree.write(path, encoding='UTF-8', xml_declaration=True)

### Indiidual Slots Handling ###

def load_slot(s_elem, show):
    '''
    Instanciates a new memslot from an Xml node.

    @param s_elem: Xml node holding the data.
    @param show:   the slot's parent show object
    @returns:      the updated show object.
    '''
    s     = MemSlot(s_elem.get('id'), show)
    s.in_ = s_elem.get('in')
    s.out = s_elem.get('out')
    # Circuits
    for c_elem in s_elem.iter("circuit"):
        s.circuits[int(c_elem.get('i'))] = c_elem.get('val')
    return s
        
def save_slot(s):
    '''
    Serialize a slot as an Xml node.

    @param s: slot to serialize.
    @returns: Xml node.
    '''
    s_elem  = ET.Element('slot')
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
    