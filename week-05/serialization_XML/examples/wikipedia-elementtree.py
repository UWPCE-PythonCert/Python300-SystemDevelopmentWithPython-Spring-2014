#!/usr/bin/env python

import bz2
import xml.etree.ElementTree as ET


if __name__ == "__main__":
    # fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000.bz2"
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    # ET.register_namespace('schemaLocation', 'http://www.mediawiki.org/xml/export-0.8/')
    tree = ET.parse(f)
    root = tree.getroot()

    # for title in root.findall('page/title'):
    for title in root.findall('{http://www.mediawiki.org/xml/export-0.8/}page/{http://www.mediawiki.org/xml/export-0.8/}title'):
        print title.text

