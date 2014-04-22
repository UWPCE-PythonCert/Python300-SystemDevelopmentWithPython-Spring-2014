#!/usr/bin/env python

import bz2
from lxml import etree

if __name__ == "__main__":
    # fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000.bz2"
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    doc = etree.parse(f)
    
    for element in doc.findall("{http://www.mediawiki.org/xml/export-0.8/}page/{http://www.mediawiki.org/xml/export-0.8/}title"):
        
        print  element.text

