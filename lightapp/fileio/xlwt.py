#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
xlwt.py

File IO routines handling the Excel format.
Most of the doc (beyond the basics) was found @
http://www.youlikeprogramming.com/2011/04/examples-generating-excel-documents-using-pythons-xlwt/

Author:  raphi <r.gaziano@gmail.com>
Created: 15/01/2012
Version: 1.0
'''
import xlwt3 as xlwt
from lightapp import utils

NUM_COLS = 5 # Columns will be 0 indexed, so set it to one less

### STYLE CONSTANTS ###
#######################

MAIN_HEADER_BORDERS = xlwt.Borders()
MAIN_HEADER_BORDERS.left   = xlwt.Borders.MEDIUM
MAIN_HEADER_BORDERS.right  = xlwt.Borders.MEDIUM
MAIN_HEADER_BORDERS.top    = xlwt.Borders.MEDIUM

MAIN_HEADER_STYLE = \
xlwt.easyxf('font: bold on, height 0x00F0; align: wrap on, vert centre, horiz center')
MAIN_HEADER_STYLE.borders = MAIN_HEADER_BORDERS

SLOT_HEADER_BORDERS = xlwt.Borders()
SLOT_HEADER_BORDERS.top   = xlwt.Borders.MEDIUM
SLOT_HEADER_BORDERS.left  = xlwt.Borders.MEDIUM
SLOT_HEADER_BORDERS.right = xlwt.Borders.MEDIUM

SLOT_HEADER_STYLE = \
xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
SLOT_HEADER_STYLE.borders = SLOT_HEADER_BORDERS

SINGLE_CELL_STYLE = xlwt.easyxf('align: horiz center')


def _get_borders(row, col, last_row):
    '''
    Figure out which borders are needed for a cell given
    its position.

    @param row:      cell's row.
    @param col:      cell's column.
    @param last_row: Bolean flag, indicating the very last row in
                     the document.
    @returns:        xlwt.Borders object.
    '''
    b = xlwt.Borders()
    b_type = xlwt.Borders.MEDIUM
    if col == 0: 
        b.left = b_type
    elif col == NUM_COLS:
        b.right = b_type
    if last_row:
        b.bottom = b_type
    return b

def write_show(show, path):
    ''' 
    Generate a .xls spreadsheet with a show's data.

    @param show: Show object to be serialized.
    @param path: File path.
    '''
    # utils.logger.debug("Saving show %s as %s"  % (show, path))
    wb = xlwt.Workbook()
    ws = wb.add_sheet(show.title)
    # General header
    ws.write_merge(0, 0, 0, NUM_COLS, 
                   "%s - Contenu mémoire" % show.title.capitalize(),
                   MAIN_HEADER_STYLE)
    row = 1
    last_slot = False
    for slot in show.slots:
        # Slot header
        ws.write_merge(row, row, 0, NUM_COLS, 
                       "Mémoire %s" % slot.id_,
                       SLOT_HEADER_STYLE)
        # Set the last_slot flag if needed (for formatting)
        last_slot = show.slots.index(slot) == len(show.slots) - 1
        last_row  = False
        row += 1
        col = 0
        remaining_cells = len([_ for _ in slot.circuits 
                                 if int(_) > 0])
        for k, v in slot.circuits.items():
            # Individual circuits
            if last_slot and col == 0 and remaining_cells < 6:
                last_row = True
            # Skip the cell if v == 0
            if not int(v):
                continue
            SINGLE_CELL_STYLE.borders = _get_borders(row, col, 
                                                     last_row)
            ws.write(row, col, "%s: %s%%" % (k+1, v), 
                     SINGLE_CELL_STYLE)
            remaining_cells -= 1
            col += 1
            if col > NUM_COLS and not last_row:
                row += 1 
                col = 0
        # Special case:
        # Close the border if the last drawn row is not full
        if col != NUM_COLS+1:
            for x in range(col, NUM_COLS + 1):
                SINGLE_CELL_STYLE.borders = _get_borders(row, x, 
                                                         last_row)
                ws.write(row, x, "", SINGLE_CELL_STYLE)
        row += 1
    wb.save(path)
