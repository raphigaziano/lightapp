#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
memslot.py

Author:  raphi <r.gaziano@gmail.com>
Created: 26/12/2012
Version: 1.0
'''

NUM_CIRC_BY_LINE = 6

class MemSlot:
    '''
    '''
    def __init__(self, num_circuits):
        
        self.id_ = None
        self.in_ = None
        self.out = None
        
        self.num_circuits = num_circuits
        self.circuits = {i: 0 for i in range(num_circuits)}
        
