
.. Documentation slides file, created by
   hieroglyph-quickstart on Tue Mar 25 16:19:30 2014.

=============
Documentation
=============

A (very) quick run down of how to document your python package.

* Chris Barker


Why
=====

Documentation is a key part of software development.

You'll be glad you have it, even if you are the only one that uses your code.

If you are writing a package you want others to use -- documentation can make all the difference

And there are some nice tools for documenting Python code.

There is even a hosting service:

 - http://readthedocs.org

Sphinx
=======

Sphinx is a documentation system build specifically for documenting Python itself:

http://spinx-doc.org

But it's also useful for any sort of structured documentation -- and is sometimes used for non-code projects.

It Produces:
 * HTML (multiple styles available)
 * PDF(via LaTeX)
 * ePub
 * man pages
 * plain text

Extendability
===============

Sphinx has an extension architecture for adding special functionality:
  * Hieroglyph (It is used for these slides...)
  
  * Matplotlib added some nice stuff:

   - http://matplotlib.org

  * Math

  * Embedded ASCII art

  * Embedding Excel spreadsheets

  * Unlimited possibilities

Automatic Documentation
========================

One of the great features of Sphinx:

It can extract docstrings from your code and build docs from them.

Includes cross referencing of modules and classes, etc.

This keeps your code and docs in sync, and encourages you to have nice docstrings.

It's a bit tricky to get it all set up though :-(

Documentation for the Documentation System
===========================================

Sphinx is, of course, documented with sphinx itself.

Its tutorial is pretty good, but can be a little confusing (particularly the autodoc stuff)

So here are a couple other resources (and many more out there):


reStructuredText
=================

reStructuredText is the markup language used for Sphinx.

Also originally developed (adapted, really) for Python documentation.

It's a plain text, easy to read and write markup.

Like many similar markup languages (Markdown, wiki markup)
 * designed to be easy to read and write
 * makes sense in palin text
 * looks a lot like what you might write in plain text anyway.

So it's suitable for use both as plain text and for fancier formatting (i.e. docstrings)

But more extensible than most others -- so good for sphinx


reStructuredText
=================

::

============================
This is the top level header
============================



reStructuredText documentation sources
=======================================

 - http://docutils.sourceforge.net/rst.html
