
.. numpy slides file, created by
   hieroglyph-quickstart on Sun Apr 27 15:13:20 2014.


**********************
Extending Python
**********************

- Chris Barker

(May 13, 2014)

.. Contents:

.. .. toctree::
..    :maxdepth: 2

Topics
=======

* Motivation

* The C API

* ctypes

* SWIG

* Cython

* Others to consider

Motivation
===========

Motivations for exiting pure Python

 - Performance
 - Integration with existing C libraries
 - Working as a glue language
 - Implement new builtin types

What is an extension module?

 - written in C (C API)
 - compiled code
 - lets you work directly with the CPython engine

Further reading:

http://docs.python.org/2/extending/extending.html

