==============================
Building Extensions to Python
==============================

To build extensions to Python, you need a C (and maybe C++) compiler that is compatible with your Python build.

Linux
======

Linux is pretty straightforward -- most systems are set up to build stuff out of the box. If not, you'll need to install the development tools. In ubuntu, that's::

   sudo apt-get install build-essential

Other systems will have something similar.

To make sure it's working, you can make sure gcc is there with::

  gcc --version

at the command line, and make sure you get something!

To compile Python extensions, you'll need the some extra files that come with python. Most distros have an extra package, called something like "python-dev" that you'll need to get the headers, etc required to build extensions::
  
  apt-get install python-dev

That should do it.

Windows:
============

The easiest way is to use the same MS compiler as the ``python.org`` build.

With Python2.7, that's MS Visual Studio 2008.

MS distributes an "express edition" for free -- find it, install it, and you should be good to go.  It can be a trick to find older additions, but googling::

    visual studio 2008 express

Got me a link direct to an installer download.

You want "Visual C++ 2008 Express Edition with SP1"

you need C and C++ compilers, but not the DB stuff, etc. Chances are you'll get more than you need, but so be it.

OS-X:
=========

Apple moves fast with its upgrades, so it's a big of a trick. The latest version of XCode is free, but does not support older systems, and thus won't work (at least not easily) for the python.org python builds.

For python.org Python2.7, you need XCode 3.* (latest is 3.2.6) 

If you have a pre-lion (10.6 or below) system, you may have gotten XCode with your install DVDs, on the extras disk or something like that. If so, I'd install from there, it's a big download.

for Lion (10.7 and above) -- you'll need to download it. Apple makes it a bit hard to find the older versions, but they can be found at:

[developer.apple.com](https://developer.apple.com/downloads)

you need to login with an AppleID (or create one), then select "Developer Tools", and search for Xcode -- poke around a bit, and you'll eventually find:

XCode 3.2.6 and iOS SDK

Download and install it (do it with a fast connection -- it's huge)

You should be good to go.

