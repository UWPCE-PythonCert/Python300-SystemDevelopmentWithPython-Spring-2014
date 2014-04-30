#!/usr/bin/env python

import bz2
from xml.dom import minidom 

if __name__ == "__main__":
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    doc = minidom.parse(f)

    element = doc.getElementsByTagName("page")[-1]
        
    el = doc.createElement('modifiedby')
    txt = doc.createTextNode('joseph')
    el.appendChild(txt)

    parent = element.parentNode
    clone = element.cloneNode(True)
    clone.appendChild(el)
    parent.appendChild(clone)

    print doc.toprettyxml(encoding="utf-8")

