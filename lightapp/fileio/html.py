#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
html.py

File IO routines handling the html format.

Author:  raphi <r.gaziano@gmail.com>
Created: 07/01/2013
Version: 1.0
"""
import os
from string import Template

HTML_TEMPLATES_DIR = os.path.join('templates', 'html')
CSS_TEMPLATES_DIR  = os.path.join('templates', 'css')

def _load_template(tmpl, path=HTML_TEMPLATES_DIR):
    '''
    '''
    with open(os.path.join(path, tmpl), 'r', 
              encoding='utf-8') as tmpl_f:
        html = tmpl_f.read()
    return Template(html)

HTML_TEMPLATES = {
    "global"   : _load_template('global.html'),
    "baseinfos": _load_template('baseinfos.html'),
    "memslot"  : _load_template('memslot.html'),
    "circuit"  : _load_template('circuit.html')
}
# Hardcoded for now
with open(os.path.join(CSS_TEMPLATES_DIR, 'style.css')) as css_f:
    CSS = css_f.read()

def serialize_show(s):
    ''' '''
    tab_infos = HTML_TEMPLATES['baseinfos'].substitute(
        title      = s.title, 
        author     = s.author, 
        date       = str(s.date), 
        nbcircuits = str(s.num_circuits)
    )

    slots_html = []
    for memslot in s.slots:
        id_ = str(memslot.id_)
        in_ = str(memslot.in_)
        out = str(memslot.out)
        circs_rows = []
        for i, v in memslot.circuits.items():
            if i % 6 == 0:
                row = []
                circs_rows.append(row)
            row.append(HTML_TEMPLATES['circuit'].substitute(
                i = str(i+1), 
                v = str(v)
            ))    

        rows_html = "".join(
            "<tr>%s</tr>" % "".join(r) for r in circs_rows
        )
        slots_html.append(HTML_TEMPLATES['memslot'].substitute(
            id_      = id_, 
            in_      = in_, 
            out      = out, 
            circuits = rows_html
        ))

    html = HTML_TEMPLATES['global'].substitute(
        style     = "<style>%s</style>" % CSS if CSS else "",
        baseinfos = tab_infos,
        memslots  = "".join(slots_html)
    )
    return html

def write_show(s, p=""):
    ''' '''
    with open(p, 'w') as f:
        f.write(serialize_show(s))