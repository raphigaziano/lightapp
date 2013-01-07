#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
html.py

File IO routines handling the html format.

Author:  raphi <r.gaziano@gmail.com>
Created: 07/01/2013
Version: 1.0
"""
# imports...
HTML_TEMPLATE = \
"""
<!-- DOCTYPE -->
<html>
    <head>
    <style>
        html {
            background-color: black;
            color: white;
        }
    </style>
    </head>
    <body>
        <table>
            %s
        </table>
        <table border='1'>
            %s
        </table>
    </body>
</html>"""
INFOS_TABLE_TEMPLATE = """
<tr>
    <th colspan='2'>%s</th>
</tr>
<tr>
    <td>Auteur:</td>
    <td>%s</td>
</tr>
<tr>
    <td>Date:</td>
    <td>%s</td>
</tr>
<tr>
    <td>Nb Circuits:</td>
    <td>%s</td>
</tr>"""
SLOT_TEMPLATE = """
<tr>
    <th colspan='2'>Id: %s</th>
    <th colspan='2'>In: %s</th>
    <th colspan='2'>Out: %s</th>
</tr>
%s"""
CIRCUIT_TEMPLATE = """
<td>n°%s: %s</td>"""

def serialize_show(s):
    ''' '''
    tab_infos = INFOS_TABLE_TEMPLATE % (
        s.title, s.author, str(s.date), str(s.num_circuits))

    slots_html = []
    for memslot in s.slots:
        id_ = str(memslot.id_)
        in_ = str(memslot.in_)
        out = str(memslot.out)
        circs_rows = []
        for i, c in memslot.circuits.items():
            if i % 6 == 0:
                row = []
                circs_rows.append(row)
            row.append(CIRCUIT_TEMPLATE % (str(i+1), str(c)))    

        rows_html = "".join(
            "<tr>%s</tr>" % "".join(r) for r in circs_rows
        )
        print(rows_html)
        slots_html.append(SLOT_TEMPLATE % (id_, in_, out, rows_html))


    html = HTML_TEMPLATE % (tab_infos, "".join(slots_html))
    return html

def write_show(s, p=""):
    ''' '''
    with open(p, 'w') as f:
        f.write(serialize_show(s))