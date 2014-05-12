#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(name = "cython_example",
      ext_modules = cythonize(['cy_add.pyx',
                               'cy_add_2.pyx',
                               'cy_add_3.pyx',
                               ])
      )

