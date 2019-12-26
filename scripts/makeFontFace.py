#!/usr/bin/env python

import os, re
from fontTools.ttLib import TTFont

EXTS = [".woff", "woff2", ".ttf", ".otf", ".svg", ".eot"]

FONT_SPECIFIER_NAME_ID = 4
FONT_SPECIFIER_FAMILY_ID = 1
def shortName( font ):
    """Get the short name from the font's names table"""
    name = ""
    family = ""
    for record in font['name'].names:
        if b'\x00' in record.string:
            name_str = record.string.decode('utf-16-be')
        else:
            name_str = record.string.decode('utf-8')

        if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
            name = name_str
        elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
            family = name_str
            
        if name and family:
            break
    return name, family

def weight( font ):
    return font['OS/2'].usWeightClass

def style(font):
    return 'italic' if (font['OS/2'].fsSelection &1 or font['head'].macStyle&2) else 'normal'

def metadata(font):
    for nrec in font['name'].names:
        name = nrec.string.decode('utf-16-be')
        print(f'{nrec.nameID} : {name}')


def cssGenerator(filename):
    root = os.path.splitext(filename)[0]
    font = TTFont(filename)
    name,family = shortName(font)
    fweight = weight(font)
    fstyle = style(font)

    #cssFile = name + "/" + name + ".css"
    template = f'''@font-face {{ 
        font-family: "{family}";
        font-weight: {fweight};
        font-style: {fstyle};
        src: url('{root}.woff') format('woff'),
             url('{root}.woff2') format('woff2'),
             url('{root}.ttf') format('ttf'),
             local('{name}');
}}'''

    return template

if __name__ == "__main__":
    args = os.sys.argv
        
    for fname in args[1:]:
        if os.path.exists(fname):
            print(cssGenerator(fname))
            
