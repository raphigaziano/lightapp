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
from string import Template #pylint: disable-msg=W0402

from lightapp import utils

CIRCS_PER_LINE = 6

HTML_TEMPLATES_DIR = os.path.join('templates', 'html')
CSS_TEMPLATES_DIR  = os.path.join('templates', 'css')

# Must be defined here so that the constants below
# can use it
def _load_template(tmpl, path=HTML_TEMPLATES_DIR):
    '''
    Load a single Html template.

    @param tmpl: Template name.
    @param path: Path to the templates directory.
                 Defaults to the HTML_TEMPLATES_DIR constant.
    @returns   : string.Template object constructed from the html
                 file. 
    '''
    # utils.logger.debug("Loading template: %s" % tmpl)
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
# Enclose CSS in <style> tags if not empty
if CSS: CSS = "<style>\n%s\n</style>" % CSS


def _tmpl_sub(tmpl, **kwargs):
    '''
    Quick helper to inject data into a template.

    @param tmpl:     Targetted template (must be a value contained
                     in the HTML_TEMPLATES dict).
    @param **kwargs: Template tags.
                     Must be passed as key=value keyword arguments.

    '''
    return HTML_TEMPLATES[tmpl].substitute(**kwargs)

def _serialize_circuits(memslot):
    '''
    Generate a Html fragment to represent a slot's circuits settings.

    @param memslot: Slot object containing the circuits to be
                    serialized.
    @returns      : Html string.
    '''
    circs_rows = []
    drawn_circs = 0
    for i, v in memslot.circuits.items():
        if drawn_circs % CIRCS_PER_LINE == 0:
            row = []
            circs_rows.append(row)
        # Skip circuits set at 0
        if int(v):
            drawn_circs += 1
        else:
            continue
        row.append(_tmpl_sub(
            'circuit',
            i = str(i+1), 
            v = str(v)
        ))   
    return "".join("<tr>%s</tr>" % "".join(r) for r in circs_rows)

def _serialize_memslots(show):
    '''
    Generate a Html fragment to represent all of a show's memory
    slots.

    @param show: Show object containing the slots to be serialized.
    @returns   : Html string.
    '''
    html = []
    for memslot in show.slots:
        id_ = str(memslot.id_)
        in_ = str(memslot.in_)
        out = str(memslot.out)

        html.append(_tmpl_sub(
            'memslot',
            id_      = id_, 
            in_      = in_, 
            out      = out, 
            circuits = _serialize_circuits(memslot)
        ))
    return "".join(html)

def serialize_show(show):
    ''' 
    Serialize a whole show to Html.

    @param show: Show object to be serialized.
    @returns   : Html document as a string.
    '''
    tab_infos = _tmpl_sub(
        'baseinfos',
        title      = show.title, 
        author     = show.author, 
        date       = utils.get_datestr(show.date), 
        nbcircuits = str(show.num_circuits)
    )
    html = _tmpl_sub(
        'global',
        style     = CSS,
        baseinfos = tab_infos,
        memslots  = _serialize_memslots(show)
    )
    return html

def write_show(s, path):
    ''' 
    Write a show's data to an html file.

    @param s:    Show object to be formatted.
    @param path: File's path.
    '''
    with open(path, 'w') as f:
        f.write(serialize_show(s))
