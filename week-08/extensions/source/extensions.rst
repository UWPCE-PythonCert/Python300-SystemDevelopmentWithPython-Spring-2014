
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

Example Case
=============

To focus on the integration techniques, rather than complex C code, we'll work with the following function we want to integrate::

  #include <stdio.h>

  int add(int x, int y) {
      return x+y;
  }
  int main(void) {
      int w = 3;
      int q = 2;
      printf("%d + %d = %d\n\n", w, q, add(w,q));
  }

This is, of course, trivial and built in to Python, but the techniques are the same.

(``week-08/extensions/code/pure-c/add.c``)

..newslide:: Building

Build it with the Makefile::

  all: add; gcc -o add add.c

::

  $ make
  gcc -o add add.c

and run it::

  $ ./add 
  3 + 2 = 5

So are simple function works -- but how to call it from Python?

The C API
=========

Write your function in pure C using the Python API and import it into Python

Good for integrating with C library functions and system calls

The API isn't trivial to learn

Lots of opportunity for error, you must do manual reference counting:
(http://docs.python.org/2/c-api/refcounting.html)

Further reading:

 - http://docs.python.org/2/extending/extending.html

 - Python 2.7 source code

Intro to the C API
===================

You'll need the Python dev package installed on your system

Pull in the Python API to your C code via::

  #include <Python.h>
  /*
  Note: Since Python may define some pre-processor definitions which
  affect the standard headers on some systems, you must include
  Python.h before any standard headers are included.

  stdio.h, string.h, errno.h, and stdlib.h are included for you.
  */

Passing Data in and out of your function
=========================================

Function arguments must be parsed on the way in and the way out

On the way in, we can call ``PyArg_ParseTuple``::

  if (!PyArg_ParseTuple(args, "s", &var1, ...))
      return NULL;

http://docs.python.org/2/c-api/arg.html#PyArg_ParseTuple

On the way out, we can call ``Py_BuildValue``::

  PyObject* Py_BuildValue(const char *format, ...)

http://docs.python.org/2/c-api/arg.html#Py_BuildValue

Registering your functions
===========================

First, register the name and address of your function in the method table::

  // Module's method table and initialization function
  static PyMethodDef AddMethods[] = {
      {"add", add, METH_VARARGS, "add two numbers"},
      {NULL, NULL, 0, NULL} // sentinel
  };

https://docs.python.org/2/extending/extending.html#the-module-s-method-table-and-initialization-function


Initializing the module
=======================

Define an initialization function::

  PyMODINIT_FUNC // does the right thing on Windows, Linux, etc.
  initadd(void) {
      // Module's initialization function
      // Will be called again if you use Python's reload()
      (void) Py_InitModule("add", AddMethods);
  }

It *must* be called ``initthe_module_name``

https://docs.python.org/2/extending/extending.html#the-module-s-method-table-and-initialization-function

The whole thing:
=================

::

  #include <Python.h>

  static PyObject *
  add(PyObject *self, PyObject *args)
  {
      int x, y, sts;

      if (!PyArg_ParseTuple(args, "ii", &x, &y))
          return NULL;
      sts = x+y;
      return Py_BuildValue("i", sts);
  }

  static PyMethodDef AddMethods[] = {
      {"add", add, METH_VARARGS, "add two numbers"},
      {NULL, NULL, 0, NULL} // sentinel
  };

  PyMODINIT_FUNC initadd(void) {
      (void) Py_InitModule("add", AddMethods);
  }

Building your extension
=========================

``distutils`` provided features for automatically building extensions::

  from distutils.core import setup, Extension
  setup(
      name='Cadd',
      version='1.0',
      description='simple c extension for an example',
      ext_modules=[Extension('add', sources=['add.c'])],
  )
Run the setup.py::

  python setup.py build_ext --inplace
(you can also just do ``install`` or ``develop`` if you want to properly installed)

Run the tests
==============

``test_add.py``::

  import pytest

  import add

  def test_basic():
      assert add.add(3,4) == 7

  def test_negative():
      assert add.add(-12, 5) == -7

  def test_float():
      with pytest.raises(TypeError):
          add.add(3, 4.0)

``$ py.test``



**********************
Subtleties we avoided:
**********************

Exception handling
===================

Works somewhat like the Unix errno variable:

* Global indicator (per thread) of the last error that occurred.
* Most functions don’t clear this on success, but will set it to indicate the cause of the error on failure.
* Most functions also return an error indicator:

  - NULL if they are supposed to return a pointer,
  - -1 if they return an integer
  - The PyArg_*() functions return 1 for success and 0 for failure (and they set the Exception for you)

The easy way to set this indicator is with PyErr_SetString

http://docs.python.org/2/c-api/exceptions.html

(you can completely control the Exception handling if you need to)


ReferenceCounting
==================

Whenever you create or no longer need a Py_Object, you need to increment or decrement the reference count:

``Py_INCREF(x)`` and ``Py_DECREF(x)``

``PyArg_ParseTuple``  and  ``Py_BuildValue``

Handle this for you.

But if you're creating new objects inside your function, you need to keep track.

And what it the function raises an exception in the middle and can't finish?

This gets really ugly and error-prone (and hard to debug!)

LAB
====

LAB 1:

* Add another function to the add.c file that multiplies two numbers instead. 
* Write some test code and make sure it works.

LAB 2:

* Find the divide module in the examples/c-api directory
* What happens when you call divide.divide(1/0)?
* This is a different result than a pure Python 1/0, which throws an exception
* Change the divide method to throw an appropriate exception in the divide-by-zero case

*******
ctypes
*******

What is ctypes?
================

A foreign function interface in Python

Binds functions in shared libraries to Python functions

Benefits:
 - Ships with Python, since 2.5
 - No new language to learn, it's all Python

Drawbacks:
 - Performance hit for on the fly type translation
 - "thicker" interface in python

Example::

  from ctypes import *
  add = cdll.LoadLibrary("add.so")
  print add.add(3,4)

Further reading:

http://docs.python.org/2/library/ctypes.html
