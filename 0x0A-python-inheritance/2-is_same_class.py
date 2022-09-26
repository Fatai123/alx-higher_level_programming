#!/usr/bin/python3
"""To check if an object is 
   exactly an instance of the specified class"""
def is_same_class(obj, a_class):
    """Arg:

        obj- object to be checked 
        a_class - The class 
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
