#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
memslot.py

Author:  raphi <r.gaziano@gmail.com>
Created: 26/12/2012
Version: 1.0
'''

class MemSlot:
    '''
    Simple structure holding a single memory slot's data.
    Individual circuits' values are stored as a (index => value)
    dictionnary.
    ''' #pylint: disable-msg=R0903
    def __init__(self, id_, parent_show):
        
        self.id_ = id_
        self.in_ = ""
        self.out = ""
        
        self.parent_show   = parent_show
        self._num_circuits = parent_show.num_circuits
        self.circuits      = {i: 0 for i in range(self._num_circuits)}

    ### Properties ###
    ##################

    @property
    def num_circuits(self):
        '''Simple setter.'''
        return self._num_circuits

    @num_circuits.setter
    def num_circuits(self, val):
        '''
        Update the circuits dictionnary according to the new
        value.
        '''
        self._num_circuits = val
        self.circuits      = {
            i: self.circuits.get(i, 0)
            for i in range(self._num_circuits)
        }
