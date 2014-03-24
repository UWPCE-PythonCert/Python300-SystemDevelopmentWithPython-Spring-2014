# -*- coding: utf-8 -*-

hello = 'Hello '
world = u'世界'

hello_world = hello + world

print type(hello_world)
print hello_world

print u"It was nice weather today: it reached 80\u00B0"

print u"Maybe it will reach 90\N{degree sign}"

print u"It is extremely rare for it ever to reach 100° in Seattle"

## encoding and decoding:

decoded = hello.decode('ascii')
print decoded

print hello.decode('ascii')


