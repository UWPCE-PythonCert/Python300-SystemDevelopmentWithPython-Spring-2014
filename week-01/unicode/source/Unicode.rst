
.. Unicode in Python 2 slides file, created by
   hieroglyph-quickstart on Thu Mar 20 20:21:45 2014.


===================
Unicode in Python 2
===================

Contents:

.. toctree::
   :maxdepth: 2

What the heck is Unicode anyway?
=================================

* First there was chaos...
* Then there was ASCII -- and all was good
  . (for English speakers, anyway)

=================================



Unicode
=================================

A good start:

The Absolute Minimum Every Software Developer Absolutely,
Positively Must Know About Unicode and Character Sets (No Excuses!)

http://www.joelonsoftware.com/articles/Unicode.html


Unicode
=================================

Everything is Bytes

If it's on disk or on a network, it's bytes

Python provides some abstractions to make it easier to deal with bytes

Unicode
=================================

Unicode is a biggie

strings vs unicode 

``str()`` vs. ``bytes()`` vs. ``unicode()`` 

(and bytearray)

python 2.x vs 3.x


(actually, dealing with numbers rather than bytes is big -- but we take that for granted)


Unicode
========

Strings are sequences of bytes

Unicode strings are sequences of platonic characters

Platonic characters cannot be written to disk or network!

(ANSI -- one character == one byte -- so easy!)

Unicode
========

the ``unicode`` object lets you work with characters

It has all the same methods as the string object.

"encoding" is converting from a unicode object to bytes

"decoding" is converting from bytes to a unicode object

(sometimes this feels backwards...)

Unicode
========

::

	import codecs
	ord()
	chr()
	unichr()
	str()
	unicode()
	codecs.encode()
	codecs.decode()

Unicode
========

::

	In [17]: u"this".encode('utf-8')
	Out[17]: 'this'

	In [18]: u"this".encode('utf-16')
	Out[18]: '\xff\xfet\x00h\x00i\x00s\x00'


Unicode Literals
=================


1) Use unicode in your source files: ::

    # -*- coding: utf-8 -*-

2) escape the unicode characters: ::

	print u"The integral sign: \u222B"
	print u"The integral sign: \N{integral}"

Lots of tables of code points online:

One example:
  http://inamidst.com/stuff/unidata/

(demo: ``code\hello_unicode.py``)

Unicode
========

Use unicode objects in all your code

decode on input

encode on output

Many packages do this for you:
    XML processing, databases, ...

Gotcha:

Python has a default encoding (usually ascii)::

  In [1]: import sys

  In [2]: sys.getdefaultencoding()
  Out[2]: 'ascii'

(``sys.getfilesystemencoding()``)

Encodings
===========

What encoding should I use???

There are a lot:

http://en.wikipedia.org/wiki/Comparison_of_Unicode_encodings

But only a couple you are likely to need:

* utf-8 *nix (ascii compatible)
* utf-16 * (Windows)

trick: 'latin-1' can hold and round-trip any binary data.

UTF-8
======

Probably the one you'll use most -- most common in internet protocols (xml, JSON, etc.)

Nice properties:

* ASCII compatible
  first 127 characters are the same
* Any ascii string is a utf-8 string
* compact for mostly-english text.

Gotchas:

* "higher" code points may use more than one byte: up to 4 for one character

* ASCII compatible means in may work with default encoding in tests -- but then blow up with real data...


Unicode
==========

Python Docs Unicode HowTo:

http://docs.python.org/howto/unicode.html

"Reading Unicode from a file is therefore simple:"::

	import codecs
	f = codecs.open('unicode.rst', encoding='utf-8')
	for line in f:
	    print repr(line)

Encodings Built-in to Python:
  http://docs.python.org/2/library/codecs.html#standard-encodings

Gotchas in Python 2
====================

Exception messages

file names, etc:
  if you pass in unicode, you get unicode::

  In [9]: os.listdir('./')
  Out[9]: ['hello_unicode.py', 'text.utf16', 'text.utf32']

  In [10]: os.listdir(u'./')
  Out[10]: [u'hello_unicode.py', u'text.utf16', u'text.utf32']


Unicode in Python 3
====================

The "string" object is unicode.

Py3 has two distict concepts:
  * "text" -- uses the unicode object
  * "binary data" -- used bytes or bytearray

Everyting that's about text is unicode.

Everything that requires binary data uses bytes.

It's all much cleaner.


Unicode LAB
==============

* Find some nifty non-ascii characters you might use.
   Create a unicode object with them in two different ways.
* In the "code" dir for this topic, there are two files::

    text.utf16
    text.utf32

read the contents into unicode objects
* write some of the text from the first exercise to file.
* item read that file back in.


reference: http://inamidst.com/stuff/unidata/


NOTE: if your terminal does not support unicode -- you'll get an error trying to print. Try a different terminal or IDE, or google for a solution




