#!/usr/bin/env python

import bz2
import logging
from xml import sax

logging.basicConfig(level=logging.INFO)
logger = logging

class WikiHandler(sax.handler.ContentHandler):
    IN_TITLE = False
    IN_USERNAME = False
    SEEN = dict()

    def startElement(self, name, attrs):
        if name == "title":
            logger.debug("in title")
            self.IN_TITLE = True
        if name == "username":
            logger.debug("in username")
            self.IN_USERNAME = True

    def characters(self, content):
        if self.IN_TITLE: 
            logger.info(content)

        if self.IN_USERNAME:
            if self.SEEN.has_key(content):
                self.SEEN[content] += 1
            else:
                self.SEEN[content] = 1

    def endDocument(self):
        for k,v in self.SEEN.iteritems():
            print "%s: %d" % (k,v)

    def endElement(self, name):
        if name == "title":
            logger.debug("out title")
            self.IN_TITLE = False
        if name == "username":
            logger.debug("out title")
            self.IN_USERNAME = False
    
if __name__ == "__main__":
    # fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000.bz2"
    fname = "data/enwiki-latest-pages-articles1.xml-p000000010p000010000-shortened.bz2"

    f = bz2.BZ2File(fname)

    handler = WikiHandler()

    sax.parse(f, handler)
