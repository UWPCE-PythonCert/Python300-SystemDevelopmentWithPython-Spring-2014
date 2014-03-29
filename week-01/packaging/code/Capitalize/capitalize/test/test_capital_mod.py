#!/usr/bin/env python

"""
test code for capitalize module

can be run with py.test or nosetests
"""

import capitalize
from capitalize import capital_mod

def test_init():
    """ makes sure it imports and can be read"""
    import capitalize
    assert hasattr(capitalize, '__version__')

def test_capitalize():
    """ test an actual string """
    capital_mod.capitalize("sample_text_file.txt", "sample_text_file_cap.txt")
    contents = open("sample_text_file_cap.txt", 'U').read()
    expected = """This Is A Really Simple Text File.
It Is Here So That I Can Test The Capitalize Script.

And That's Only There To Try Out Distutils.

So There."""
    assert contents.strip() == expected 

    

