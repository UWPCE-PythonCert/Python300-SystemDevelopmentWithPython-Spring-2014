
.. __new__ slides file, created by
   hieroglyph-quickstart on Mon Mar 31 23:06:53 2014.


========
__new__
========

Chris Barker

``PythonCHB@gmail.com``

.. toctree::
   :maxdepth: 2

Class Creation
================

What happens when a class instance is created?

::

	class Class(object):
	    def __init__(self, arg1, arg2):
	        self.arg1 = arg1
	        self.arg2 = arg2
	        .....

* A new instance is created
* ``__init__`` is called
* The code in ``__init__`` is run to initialize the instance


Class Creation
=================

What if you need to do something before creation?

Enter: ``__new__``

::

	class Class(object):
	    def __new__(cls, arg1, arg2):
	        some_code_here
	        return cls()
	        .....

* ``__new__`` is called: it returns a new instance
* The code in ``__new__`` is run to pre-initialize
* ``__init__`` is called
* The code in ``__init__`` is run to initialize the instance


Class Creation
================

``__new__`` is a static method -- but it must be called with a class object as the first argument. And it should return a class instance:

::

	class Class(superclass):
	    def __new__(cls, arg1, arg2):
	        some_code_here
	        return superclass.__new__(cls)
	        .....


When would  you need to use it:

* subclassing an immutable type:\\

  - It's too late to change it once you get to ``__init__``

* When ``__init__`` is not called:

  - unpickling

  - copying

You may need to put some code in ``__new__`` to make sure things go right 

More detail here:

\url{http://www.python.org/download/releases/2.2/descrintro/#__new__
\end{frame 

LAB
====

Demo: ``code/__new__/new_example.py``

Write a subclass of int that will always be an even number: round the input to the closest even number

``code/__new__/even_int.py``


