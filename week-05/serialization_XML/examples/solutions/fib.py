#!/usr/bin/env python

class FibIterator(object):

    def __init__(self, count):
        self.values = [0,1]
        self.i = 0
        self.count = count

    def __iter__(self):
        return self

    def next(self):
        if self.i >= self.count:
            raise StopIteration

        self.i += 1
        new_value = sum(self.values)
        self.values.append(new_value)
        return self.values.pop(0)

import sys

iter = FibIterator(int(sys.argv[1]))
for i,x in enumerate(iter):
    print "%d: %d" % (i+1,x)
