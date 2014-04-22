#!/usr/bin/env python

import bz2
from xml.dom import minidom 

if __name__ == "__main__":
    fname = "data/billion_lolz.xml"

    doc = minidom.parse(fname)
