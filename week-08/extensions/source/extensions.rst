
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


Calling functions with ctypes
==============================

The shared lib must be loaded::

    add = ctypes.cdll.LoadLibrary("add.so")

An already loaded lib can be loaded with:

    libc = ctypes.CDLL("/usr/lib/libc.dylib")

ctypes comes with a utility to help find libs::

    ctypes.util.find_library(name)

(good for system libs)

.. nextslide::

Once loaded, a ctypes wrapper around a c function can be called directly::

    print add.add(3,4)

But....


C is statically typed -- once compiled, the function must be called with the correct types.

ctypes Data Types
=================

ctypes will auto-translate these native types:

  - ``None``
  - int
  - byte strings (``bytes()``, ``str()``)
  - ``unicode`` (careful! unicode is ugly in C!)

These can be directly used as parameters when calling C functions.

.. nextslide::

Most types must be wrapped in a ctypes data type::

    printf("An int %d, a double %f\n", 1234, c_double(3.14))

There are ctypes wrappers for all the "standard" C types

http://docs.python.org/2/library/ctypes.html#fundamental-data-types


You can also do pointers to types::

    a_lib.a_function( ctypes.byref(c_float(x)))

http://docs.python.org/2/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference

.. nextslide:: C structs

You can define C structs::

  >>> class POINT(ctypes.Structure):
  ...     _fields_ = [("x", ctypes.c_int),
  ...                 ("y", ctypes.c_int)]
  ...
  >>> point = POINT(10, 20)
  >>> print point.x, point.y
  10 20
  >>> point = POINT(y=5)
  >>> print point.x, point.y
  0 5

.. nextslide:: Custom Python Classes 

You can define how to pass data from your custom classes to ctypes:

Define an ``_as_parameter_`` attribute (or property)::

  class MyObject(object):
      def __init__(self, number):
          self._as_parameter_ = number

  obj = MyObject(32)
  printf("object value: %d\n", obj)

http://docs.python.org/2/library/ctypes.html#fundamental-data-types

(careful with types here!)

.. nextslide:: Return Types

To defining the return type, define the ``restype`` attribute.

Pre-defining the entire function signature::

  libm.pow.restype = ctypes.c_double
  libm.pow.argtypes = [ctypes.c_double, ctypes.c_double]

And you can just call it like a regular python function -- ctypes will type check/convert at run time::

  In [10]: libm.pow('a string', 4)
  ---------------------------------------------------------------------------
  ArgumentError                             Traceback (most recent call last)
  <ipython-input-10-01be690a307b> in <module>()
  ----> 1 libm.pow('a string', 4)

  ArgumentError: argument 1: <type 'exceptions.TypeError'>: wrong type

Some more features
===================

Defining callbacks into Python code from C::

    ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

http://docs.python.org/2/library/ctypes.html#ctypes.CFUNCTYPE

Numpy provides utilities for numpy arrays:

http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html

(works well for C code that takes "classic" C arrays)


Summary:
========

* ``ctypes`` allows you to call shared libraries:

  - Your own custom libs
  - System libs
  - Proprietary libs

* Supports almost all of C:
 
 - Custom data types

   - structs 
   - unions
   - pointers

 - callbacks

.. nextslide::

* Upside:

  - You can call system libs with little code
  - You don't need to compile anything

    - at least for system and pre-compiled libs

* Downsides:

  - You need to specify the interface

    - and it is NOT checked for you!

  - Translation is done on the fly at run time

    - performance considerations

LAB
====

In ``code/ctypes`` you'll find ``add.c``

You can build a shared lib with it with ``make``
(``make.bat``) on Windows.

``test_ctypes.py`` will call that dll, and a few system dlls.

* Take a look at what's there, and how it works.
* add another function to add.c, that takes different types (maybe divide?)
* rebuild, and figure out how to call it with ctypes.

* Try calling other system functions with ctypes.


*******
Cython
*******

A Python like language with static types which compiles down to C code for Python extensions.

Cython
=======

* Can write pure python
  - Fully understands the python types

* With careful typing -- you get pure C (and pure C speed)

* Can also call other C code: libraries or compiled in.

* Used for custom Python extensions and/or call C and C++ code.

.. nextslide::

Further reading:

Web site:

  http://www.cython.org/

Documentation:

  http://docs.cython.org/

Wiki:

  https://github.com/cython/cython/wiki



Developing with Cython
========================

First, install cython with::

 ``pip install cython``

Cython files end in the .pyx extension. An example add.pyx::

  def add(int x, int y):
      cdef int result=0
      result = x + y
      return result


Basic Cython
=============

Cython functions can be declared three ways::

  def foo # callable from Python

  cdef foo # only callable from Cython/C
  
  cpdef foo # callable from both Cython and Python

Once your .pyx file is created, it is converted to C via


cython cy_add.pyx
Generate "annoted" C code in HTML


cython -a cy_add.pyx
To build your Python extension:


python cy_setup.py build_ext --inplace # note Cython defines its' own build_ext in Cython.Distutils.build_ext

Cython can compile pure Python code to C to provide a performance improvement



::




Consider a more expensive function


def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx


Impovements with static typing

Convert the dynamically typed variables to static types and measure performance improvement before and after
Can static types and dynamic types be mixed?
Check the performance in converting the function type to static (see here)
Use cython -a to compare the generated C code in all cases

def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx



