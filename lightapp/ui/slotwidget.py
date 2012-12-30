#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

from lightapp.ui.QDesigner import SlotWidget

CIRCS_PER_LINE = 6
 
class SlotWidget(QtGui.QWidget, SlotWidget.Ui_SlotWidget):
    '''
    '''
    def __init__(self, parent=None, slot=None):
        super(SlotWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.slot = slot
        #Move?
        self.gBox_circuits.setLayout(self.cboxes_layout)
        self._init_circuits_cboxes()

    def _init_circuits_cboxes(self):
        ''' '''
        y = -1
        for i, slot  in self.slot.circuits.items():
            widget = QtGui.QWidget(self)
            widget.setFixedWidth(80) # USE CONST
            widget.setSizePolicy(QtGui.QSizePolicy.Fixed, 
                                 QtGui.QSizePolicy.Fixed)
            
            line_layout = QtGui.QHBoxLayout()
            widget.setLayout(line_layout)

            label = QtGui.QLabel("%d: " % (i+1), widget)
            cbox  = QtGui.QComboBox(widget)
            cbox.setEditable(True)
            # USE CONST
            cbox.addItems([str(x) for x in range(101) if x % 5 == 0])

            line_layout.addWidget(label)
            line_layout.addWidget(cbox)
            # Widget position
            x = i % CIRCS_PER_LINE
            if i % CIRCS_PER_LINE == 0: 
                y += 1
                # grow groupbox
                if y > 0:
                    h_incr = widget.height() + 5 # USE CONST
                    self.setFixedHeight(self.height() + h_incr)
                    self.gBox_circuits.setFixedHeight(
                        self.gBox_circuits.height() + h_incr)
            self.cboxes_layout.addWidget(widget, y, x)
