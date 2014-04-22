#!/usr/bin/env python

import bz2
import logging
from xml import sax

logging.basicConfig(level=logging.INFO)
logger = logging

class WikiHandler(sax.handler.ContentHandler):
    IN_TITLE = False

    def startElement(self, name, attrs):
        if name == "title":
            logger.debug("in title")
            self.IN_TITLE = True

    def characters(self, content):
        if self.IN_TITLE: 
            logger.info(content)

    def endElement(self, name):
        if name == "title":
            logger.debug("out title")
            self.IN_TITLE = False
    
if __name__ == "__main__":
    # fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000.bz2"
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    handler = WikiHandler()

    sax.parse(f, handler)
