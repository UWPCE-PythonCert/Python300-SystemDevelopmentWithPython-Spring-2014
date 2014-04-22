#!/usr/bin/env python

import bz2
from xml.dom import minidom 

if __name__ == "__main__":
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    doc = minidom.parse(f)

    for element in doc.getElementsByTagName("title"):
        
        text_node = element.childNodes[0]
        print text_node.data

