#!/usr/bin/python
# -*- coding: utf-8 -*-

import sip
from PyQt4 import QtGui, QtCore

from lightapp.ui.QDesigner import SlotsWindow
from lightapp.ui import slotwidget
 
class SlotWindow(QtGui.QDialog, SlotsWindow.Ui_Dialog):
    '''
    '''
    def __init__(self, show):
        super(SlotWindow, self).__init__()
        self.setupUi(self)
        self._show = show
        
        # Couldn't assign the layout right in the designer for some
        # reason
        self.scrollAreaWidgetContents.setLayout(self.scroller_layout)
        
        if not self._show.slots:
            self.add_slot()
        else:
            self.load_slots()
            
        self.connect_events()
        
    def add_slot(self, slot=None):
        ''' '''
        s = slot or self._show.add_slot()
        print("adding slot %s" % (s.id_))
        # create slot_widget
        sw = slotwidget.SlotWidget(self, s)
        self.scroller_layout.addWidget(sw)
        
        # auto scroll down
        scroll_bar = self.slots_scroller.verticalScrollBar()
        # scrollBar.setMaximum(len(txt)-1)
        scroll_bar.setMaximum(sw.height() * len(self._show.slots))
        scroll_bar.setValue(scroll_bar.maximum())

        # Assuming any provided slot means its loaded from a save
        if slot is None:
            self._show.slot_modify()
        # Focus the id field
        # sw.txtBox_slot_id.setSelection(0, 500)
        
    def load_slots(self):
        ''' '''
        for slot in self._show.slots:
            self.add_slot(slot)
        
    def update_slot(self):
        ''' '''
        print('updating slots...')
        for s in self.findChildren(slotwidget.SlotWidget):
            s.update_slot()

    def remove_slot(self, slot_widget):
        ''' '''
        self._show.remove_slot(slot_widget.slot)
        self.scroller_layout.removeWidget(slot_widget)
        # This way of deleting a widget is apparently cleaner
        # if said widget has children.
        # cf http://stackoverflow.com/questions/5899826/pyqt-how-to-remove-a-widget
        sip.delete(slot_widget)

    def connect_events(self):
        '''Actions/Functions connections'''
        self.connect(self.btn_add_slot, QtCore.SIGNAL("clicked()"),
                     self.add_slot)

    def accept(self):
        ''' '''
        self.update_slot()
        super(SlotWindow, self).accept()
        
