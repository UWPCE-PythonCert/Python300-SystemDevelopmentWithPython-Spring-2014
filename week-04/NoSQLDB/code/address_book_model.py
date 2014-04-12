#!/usr/bin/env python

"""
sample data for NOSQL examples

This version has some real structure to it: A more complicated data model

"""

class Person(object):
    """
    class to represent an individual person
    """
    def __init__(self,
                 last_name,
                 first_name=''
                 middle_name=''
                 cell_phone=''
                 home=None.
                 work=None,
                 ):
        """
        initialize a Person object:
        """ 
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.cell_phone = cell_phone
        self.home = home
        self.work = business

class Address(object):
    """
    class that represents an address
    """
    def __init__(self,
                 line_1='',
                 line_2='',
                 city='',
                 state=''
                 zip='',
                 )
    self.line_1=line_1
    self.line_2=line_2
    self.city=city
    self.state=state
    self.zip_code=zip_code

class Location(object):
    """
    class that represents a location: home or business
    """
    def __init__(self,
                 address=None,
                 email=None,
                 phone=None,
                 )

class Household(object):
    """
    Class that represents a Household.

    A household has one or more people, and a Location
    """

    def _init__(self,
                people=(),
                location=None,
                ):
    people = list(people)
    location = location


AddressBook = [ {'first_name': "Chris",
                 'last_name': "Barker",
                 'address' : {'line_1':"835 NE 33rd St",
                              'line_2' : "",
                              'city' : "Seattle",
                              'state': "WA",
                              'zip': "96543"},
                 'email' : "PythonCHB@gmail.com",
                 'home_phone' : "206-555-1234",
                 'office_phone' : "123-456-7890",
                 'cell_phone' : "234-567-8901",
                 },
                
                {'first_name': "Fred",
                 'last_name': "Jones",
                 'address' : {'line_1':"123 SE 13th St",
                              'line_2' : "Apt. 43",
                              'city' : "Tacoma",
                              'state': "WA",
                              'zip': "93465"},
                 'email' : "FredJones@some_company.com",
                 'home_phone' : "510-555-1234",
                 'office_phone' : "564-466-7990",
                 'cell_phone' : "403-561-8911",
                 },
                
                {'first_name': "Nancy",
                 'last_name': "Wilson",
                 'address' : {'line_1':"8654 Walnut St",
                              'line_2' : "Suite 567",
                              'city' : "Pasadena",
                              'state': "CA",
                              'zip': "12345"},
                 'email' : "Wilson.Nancy@gmail.com",
                 'home_phone' : "423-321-9876",
                 'office_phone' : "123-765-9877",
                 'cell_phone' : "432-567-8466",
                 },
                ]

