#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
slotwidget.py

Author:  raphi <r.gaziano@gmail.com>
Created: ??/12/2012
Version: 1.0
'''
from PyQt4 import QtGui, QtCore

from lightapp.ui.QDesigner import SlotWidget as swidget

### Constants ###
#################

WIDGET_WIDTH = 80
CBOX_ROWS_V_SPACING = 5

CIRCS_PER_LINE = 6
CIRC_ITEMS     = [str(x) for x in range(0, 101, 5)]
IN_ITEMS       = [str(x / 10) for x in range(101)]
IN_ITEMS      += [str(x) for x in range(12, 101, 2)]
OUT_ITEMS      = [str(x / 10) for x in range(101)]
OUT_ITEMS     += [str(x) for x in range(12, 101, 2)]


class SlotWidget(QtGui.QWidget, swidget.Ui_SlotWidget):
    '''
    Memory Slot editing widget.
    Responsible for editing its own MemSlot object.
    Generated and displayed dynamically by the SlotsWin form.
    '''
    def __init__(self, parent=None, slot=None):
        super(SlotWidget, self).__init__(parent)
        self.setupUi(self)

        self.slot      = slot
        self._slot_win = self.parent()

        self.init_components()
        self.init_fields()
        self.connect_event()

    def init_components(self):
        '''
        Sets up the widget's components
        (mainly the comboboxes lists of values).
        '''
        self.txtBox_slot_id.setText(str(self.slot.id_))
        # Assign list copies just to be safe
        self.cBox_in.addItems(IN_ITEMS[:])
        self.cBox_out.addItems(OUT_ITEMS[:])

        self.gBox_circuits.setLayout(self.cboxes_layout)

        self._init_circuits_cboxes()
        # Icon created here because QtDesigner won't let me use
        # a common ressource file.
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/img/cross.png"))
        self.btn_supr.setIcon(icon)

    def _init_circuits_cboxes(self):
        '''
        Dynamic generation of n comboboxes, n being the number
        of circuits needed.
        '''
        y = -1
        for i, _ in self.slot.circuits.items():
            widget = QtGui.QWidget(self.gBox_circuits)
            widget.setFixedWidth(WIDGET_WIDTH)
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
            if x == 0: # CHECK
                y += 1
                if y > 0: # grow groupbox
                    h_incr = widget.height() + CBOX_ROWS_V_SPACING
                    self.setFixedHeight(self.height() + h_incr)
                    self.gBox_circuits.setFixedHeight(
                        self.gBox_circuits.height() + h_incr)
            self.cboxes_layout.addWidget(widget, y, x)

    def _get_circuit_cboxes(self):
        '''
        Yields every circuit's combobox.
        Usage:
        for cb in self._get_circuit_cboxes():
            # do stuff with cb

        @returns: Generator object
        '''
        for w in self.gBox_circuits.children():
            cb = w.findChild(QtGui.QComboBox)
            if cb is None:
                continue
            yield cb

    def _set_cbox(self, cbox, val, deflist=None):
        '''
        Helper for setting a combobox value.
        It will first try to set the cb's index to point to the 
        passed value, and then set the cb's text field if val is not
        among the default values.

        @param cbox:    The combobox to set.
        @param val:     Desired value.
        @param deflist: Optional. List of default values to try and 
                        pick the index from.
        '''
        if deflist is not None:
            try:
                cbox.setCurrentIndex(deflist.index(val))
            except ValueError:
                return self._set_cbox(cbox, val)
        else:
            cbox.lineEdit().setText(val)

    def init_fields(self):
        '''Update the widget's fields from the slot's attrs'''
        self.txtBox_slot_id.setText(str(self.slot.id_))
        if self.slot.in_:
            self._set_cbox(self.cBox_in, self.slot.in_, IN_ITEMS)
        if self.slot.out:
            self._set_cbox(self.cBox_out, self.slot.out, OUT_ITEMS)
        # Circuits
        for i, cb in enumerate(self._get_circuit_cboxes()):
            val = self.slot.circuits[i]
            if val:
                self._set_cbox(cb, val, CIRC_ITEMS)

    def update_slot(self):
        '''Update the slot object from the form's fields.'''
        self.slot.id_ = self.txtBox_slot_id.text()
        self.slot.in_ = self.cBox_in.currentText()
        self.slot.out = self.cBox_out.currentText()
        for i, cb in enumerate(self._get_circuit_cboxes()):
            self.slot.circuits[i] = cb.currentText()

    def remove(self):
        '''Delete self and the associated memory slot'''
        self._slot_win.remove_slot(self)

    def connect_event(self):
        '''Signals/Functions connections'''
        # Show modifying events
        self.connect(self.txtBox_slot_id,
                     QtCore.SIGNAL('textEdited(const QString&)'),
                     self.slot.parent_show.slot_modify)

        self.connect(self.cBox_in,
                     QtCore.SIGNAL(
                        'currentIndexChanged(const QString&)'),
                     self.slot.parent_show.slot_modify)
        self.connect(self.cBox_in,
                     QtCore.SIGNAL(
                        'editTextChanged(const QString&)'),
                     self.slot.parent_show.slot_modify)
        self.connect(self.cBox_out,
                     QtCore.SIGNAL(
                        'currentIndexChanged(const QString&)'),
                     self.slot.parent_show.slot_modify)
        self.connect(self.cBox_out,
                     QtCore.SIGNAL(
                        'editTextChanged(const QString&)'),
                     self.slot.parent_show.slot_modify)
        # Circuits comboboxes
        for cb in self._get_circuit_cboxes():
            self.connect(cb,
                         QtCore.SIGNAL(
                            'currentIndexChanged(const QString&)'),
                         self.slot.parent_show.slot_modify)
            self.connect(cb,
                         QtCore.SIGNAL(
                            'editTextChanged(const QString&)'),
                         self.slot.parent_show.slot_modify)
        # Parent window's slot supression method
        self.connect(self.btn_supr,
                     QtCore.SIGNAL('clicked()'),
                     self.remove)
