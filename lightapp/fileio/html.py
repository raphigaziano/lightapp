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

# Must be defined here so that the constants below
# can use it
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

def _tmpl_sub(tmpl, **kwargs):
    '''
    Quick helper to inject data into a template.

    @param tmpl:     targetted template (must be a value contained
                     in the HTML_TEMPLATES dict).
    @param **kwargs: template tags
    '''
    return HTML_TEMPLATES[tmpl].substitute(**kwargs)


def serialize_show(s):
    ''' '''
    tab_infos = _tmpl_sub(
        'baseinfos',
        title      = s.title, 
        author     = s.author, 
        date       = str(s.date), 
        nbcircuits = str(s.num_circuits)
    )
    # Well that was straight-forward enough, now let's have fun:
    slots_html = []
    for memslot in s.slots:
        id_ = str(memslot.id_)
        in_ = str(memslot.in_)
        out = str(memslot.out)

        circs_rows = []
        for i, v in memslot.circuits.items():
            if i % 6 == 0: # @FIXME Magic number
                row = []
                circs_rows.append(row)
            row.append(_tmpl_sub(
                'circuit',
                i = str(i+1), 
                v = str(v)
            ))    

        rows_html = "".join(
            "<tr>%s</tr>" % "".join(r) for r in circs_rows
        )
        slots_html.append(_tmpl_sub(
            'memslot',
            id_      = id_, 
            in_      = in_, 
            out      = out, 
            circuits = rows_html
        ))

    html = _tmpl_sub(
        'global',
        style     = "<style>%s</style>" % CSS if CSS else "",
        baseinfos = tab_infos,
        memslots  = "".join(slots_html)
    )
    return html

def write_show(s, p=""):
    ''' '''
    path = p or "%s%s.html" % (p, s.title)
    with open(path, 'w') as f:
        f.write(serialize_show(s))
