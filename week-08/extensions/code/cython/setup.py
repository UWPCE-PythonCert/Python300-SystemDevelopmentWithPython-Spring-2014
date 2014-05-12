#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# ext_1 = Extension("cy_add",   ["cy_add.pyx"])
# ext_2 = Extension("cy_add_2", ["cy_add_2.pyx"])
# #ext_3 = Extension("cy_add_3", ["cy_add_3.pyx", "add.c"])
# ext_3 = Extension("cy_add_3", ["cy_add_3.pyx"])

# extensions = [ext_1,
#               ext_2,
#               ext_3,
#               ]

setup(name = "cython_example",
      ext_modules = cythonize(['cy_add.pyx',
                               'cy_add_2.pyx',
                               'cy_add_3.pyx',
                               ])
      )

