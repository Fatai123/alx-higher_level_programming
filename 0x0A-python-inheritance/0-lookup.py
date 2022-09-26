#!/usr/bin/python3
'''Function that returns the list of
   available attributes and methods of an object
'''
def lookup(obj):
    """Args:
            -obj: object to look into
       Result:
            -return: The list of attribute and object
    """
    return dir(obj)
