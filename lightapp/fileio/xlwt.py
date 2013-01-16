#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
xlwt.py

File IO routines handling the Excel format.

Author:  raphi <r.gaziano@gmail.com>
Created: 15/01/2012
Version: 1.0
'''
import xlwt3 as xlwt

def write_show(show, path):
    ''' '''
    wb = xlwt.Workbook()
    ws = wb.add_sheet(show.title)
    # General header
    ws.write_merge(0, 0, 0, 5, "%s - Contenu mémoire" % show.title)
    row = 1
    for slot in show.slots:
        # Slot header
        ws.write_merge(row, row, 0, 5, "Mémoire %s" % slot.id_)
        row += 1
        col = 0
        for k, v in slot.circuits.items():
            # Individual circuits, skipped if set at 0
            if v == "0":
                continue
            ws.write(row, col, "%s: %s%%" % (k+1, v))
            col += 1
            if col == 6:
                row +=1 
                col = 0
        row += 1
    wb.save(path)