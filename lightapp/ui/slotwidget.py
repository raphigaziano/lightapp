#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore

from lightapp.ui.QDesigner import SlotWidget
# Copied from puic4 generated code to use the main window's
# ressource file.
# @TODO: See if there's a cleaner way to reuse the rc file
import ressources_rc
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

### Constants ###

CIRCS_PER_LINE = 6
CIRC_ITEMS     = [str(x) for x in range(0, 101, 5)]
IN_ITEMS       = ["???" for __ in range(10)]
OUT_ITEMS      = ["???" for __ in range(10)]


class SlotWidget(QtGui.QWidget, SlotWidget.Ui_SlotWidget):
    '''
    '''
    def __init__(self, parent=None, slot=None):
        super(SlotWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.slot = slot
        
        self.init_components()
        self.init_fields()
        self.connect_event()

    def init_components(self):
        ''' '''
        self.txtBox_slot_id.setText(str(self.slot.id_))
        # Assign list copies just to be safe
        self.cBox_in.addItems(IN_ITEMS[:])
        self.cBox_out.addItems(OUT_ITEMS[:])
        
        self.gBox_circuits.setLayout(self.cboxes_layout)

        self._init_circuits_cboxes()

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/icons/img/cross.png")))
        self.btn_supr.setIcon(icon)

    def _init_circuits_cboxes(self):
        ''' '''
        y = -1
        for i, slot  in self.slot.circuits.items():
            widget = QtGui.QWidget(self.gBox_circuits)
            widget.setFixedWidth(80) # USE CONST
            widget.setSizePolicy(QtGui.QSizePolicy.Fixed, 
                                 QtGui.QSizePolicy.Fixed)
            
            line_layout = QtGui.QHBoxLayout()
            widget.setLayout(line_layout)

            label = QtGui.QLabel("%d: " % (i+1), widget)
            cbox  = QtGui.QComboBox(widget)
            cbox.setEditable(True)
            # Assign a copy to be safe
            cbox.addItems(CIRC_ITEMS[:])

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

    def _get_circuit_cboxes(self):
        ''' '''
        for w in self.gBox_circuits.children():
            cb = w.findChild(QtGui.QComboBox)
            if cb is None: 
                continue
            yield cb

    def init_fields(self):
        ''' '''
        self.txtBox_slot_id.setText(str(self.slot.id_))
        if self.slot.in_:
            self.cBox_in.setCurrentIndex(
                IN_ITEMS.index(self.slot.in_))
        if self.slot.out:
            self.cBox_out.setCurrentIndex(
                OUT_ITEMS.index(self.slot.out))
        # Circuits
        for i, cb in enumerate(self._get_circuit_cboxes()):
            val = self.slot.circuits[i]
            if val:
                cb.setCurrentIndex(CIRC_ITEMS.index(val))

    def update_slot(self):
        ''' '''
        self.slot.id_ = self.txtBox_slot_id.text()
        self.slot_in_ = self.cBox_in.currentText()
        self.slot.out = self.cBox_out.currentText()
        for i, cb in enumerate(self._get_circuit_cboxes()):
            self.slot.circuits[i] = cb.currentText()

    def connect_event(self):
        ''' '''
        # Show modifying events
        self.connect(self.txtBox_slot_id, 
                     QtCore.SIGNAL('textEdited(const QString&)'),
                     self.slot.parent_slot.slot_modify)

        self.connect(self.cBox_in, 
                     QtCore.SIGNAL(
                        'currentIndexChanged(const QString&)'),
                     self.slot.parent_slot.slot_modify)
        self.connect(self.cBox_in, 
                     QtCore.SIGNAL(
                        'editTextChanged(const QString&)'),
                     self.slot.parent_slot.slot_modify)
        self.connect(self.cBox_out, 
                     QtCore.SIGNAL(
                        'currentIndexChanged(const QString&)'),
                     self.slot.parent_slot.slot_modify)
        self.connect(self.cBox_out, 
                     QtCore.SIGNAL(
                        'editTextChanged(const QString&)'),
                     self.slot.parent_slot.slot_modify)
        # Circuits comboboxes
        for cb in self._get_circuit_cboxes():
            self.connect(cb, 
                         QtCore.SIGNAL(
                            'currentIndexChanged(const QString&)'),
                         self.slot.parent_slot.slot_modify)
            self.connect(cb, 
                         QtCore.SIGNAL(
                            'editTextChanged(const QString&)'),
                         self.slot.parent_slot.slot_modify)