
.. super() slides file, created by
   hieroglyph-quickstart on Mon Mar 31 23:05:05 2014.

=======
super()
=======

Chris Barker

``PythonCHB@gmail.com``

.. toctree::
   :maxdepth: 2



Multiple Inheritance
======================

Multiple inheritance:

  Pulling from more than one class

::

	class Combined(Super1, Super2, Super3):
	    def __init__(self, something, something else):
	        Super1.__init__(self, ......)        
	        Super2.__init__(self, ......)        
	        Super3.__init__(self, ......)        

(calls to the super classes ``__init__`` are optional and case dependent)


Multiple Inheritance
=====================

Method Resolution Order  left to right

1. Is it an instance attribute ?

2. Is it a class attribute ?

3. Is it a superclass attribute ?

   a. is it an attribute of the left-most superclass?

   b. is it an attribute of the next superclass?

   c. ``....``

4. Is it a super-superclass attribute ?

5. also left to right...


( This can get complicated...more on that later...)

Mix-ins
=========

Why would you want to do this?


Hierarchies are not always simple:


* Animal
  
  * Mammal
    
    * GiveBirth()
    
  * Bird
    
    * LayEggs()
    
Where do you put a Platypus or an Armadillo?


Real World Example: ``wxPython FloatCanvas``


The Diamond Problem 
=====================

::

	class A(object):
	    def do_your_stuff(self):
	        print "doing A's stuff"
	    
	class B(A):
	    def do_your_stuff(self):
	        A.do_your_stuff(self)
	        print "doing B's stuff"
	    
	class C(A):
	    def do_your_stuff(self):
	        A.do_your_stuff(self)
	        print "doing C's stuff"

	class D(B,C):    
	    def do_your_stuff(self):
	        B.do_your_stuff(self)
	        C.do_your_stuff(self)
	        print "doing D's stuff"


The Diamond Problem 
=====================

Multiple paths to the same superclass:

.. image:: /_static/Diamond_inheritance.png
    :align: center
    :height: 400px

A's methods can get called twice.

(demo: ``code/diamond.py``)

The Method Resolution Order
============================

Python's The Method Resolution Order ( MRO ) is defined by the C3 linearization algorithm:

http://en.wikipedia.org/wiki/C3_linearization.

In C3, only the last occurrence of a given class is retained.

In short: corrects the multiple calls to the same method problem

The classic description of modern MRO by Guido:
http://www.python.org/download/releases/2.2.2/descrintro/#mro, 

And one more:
http://www.python.org/download/releases/2.3/mro/

demo: ``__mro__``

super()
========

Getting the superclass: ::

	class SafeVehicle(Vehicle):
	    """
	    Safe Vehicle subclass of Vehicle base class...
	    """
	    def __init__(self, position=0, velocity=0, icon='S'):
	        Vehicle.__init__(self, position, velocity, icon)


``Vehicle`` is repeated here -- what if we wanted to change the superclass?

And there were a bunch of references to Vehicle?

 
super()
========

Getting the superclass: ::

	class SafeVehicle(Vehicle):
	    """
	    Safe Vehicle subclass of Vehicle base class
	    """
	    def __init__(self, position=0, velocity=0, icon='S'):
	        super(SafeVehicle, self).__init__(position, velocity, icon)



``super`` is about more than just making it easier to refactor.

Remember the method resolution order? 

And the diamond problem?
 


What does super() do?
======================

``super`` returns a "proxy object" that delegates method calls.


It's not returning the object itself -- but you can call methods on it.


It runs through the method resolution order (MRO) to find the method you call.


Key point: the MRO is determined *at run time*


http://docs.python.org/2/library/functions.html#super

 
What does super() do?
======================

Not the same as calling one superclass method: ``super()`` will call all the sibling superclass methods: ::

	class D(C, B, A):
	    def __init__(self):
	       super(D, self).__init__()

same as::

	class D(C, B, A):
	    def __init__(self):
	       C.__init__()
	       B.__init__()
	       A.__init__()

| You may not want that --
| demo: ``code /super_test.ipnb``

super()
=======

Two seminal articles about ``super()``:


"*Super Considered Harmful*"

  - James Knight 

https://fuhm.net/super-harmful


"*super() Considered Super!*"

  - Raymond Hettinger 


http://rhettinger.wordpress.com/2011/05/26/super-considered-super


(Both worth reading....)
 

super() issues...
=================

Both actually say similar things:

* The method being called by super() needs to exist
* Every occurrence of the method needs to use super():

  - Use it consistently, and document that you use it, as it is part of the external interface for your class, like it or not.

calling super():
=================

The caller and callee need to have a matching argument signature:
  
Never call super with anything but the exact arguments you received, unless you really know what you're doing.

If you add one or more optional arguments, always accept::

	*args, **kwargs

and call super like::

	super(MyClass, self).method(args_declared, *args, **kwargs)
  

Wrap Up
=========

Thinking OO in Python:


Think about what makes sense for your code:

* Code re-use
* Clean APIs
* ... 


Don't be a slave to what OO is *supposed to look like*.


Let OO work for you, not *create* work for you.


Wrap Up
========

OO in Python:


*The Art of Subclassing*:  -- Raymond Hettinger


  http://pyvideo.org/video/879/the-art-of-subclassing


"classes are for code re-use -- not creating taxonomies"


*Stop Writing Classes*:  -- Jack Diederich


http://pyvideo.org/video/880/stop-writing-classes

"If your class has only two methods and one of them is ``__init__`` -- you don't need a class"

and 

"I hate code: I want as little of it in our product as possible"


