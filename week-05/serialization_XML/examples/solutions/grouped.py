import itertools

items = itertools.chain(xrange(10), FibIterator(10))
# sort the items for groupby:
sorted_items = sorted(items)
grouped_items = itertools.groupby(sorted_items)
for key, it in grouped_items:
    print "%s: " % key
    for x in it:
        print "\t%s " % x
