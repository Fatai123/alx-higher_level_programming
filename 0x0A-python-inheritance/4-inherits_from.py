#!/usr/bin/python3
"""Check if the object is an instance of 
   a class that inherited (directly or indirectly)
   from the specified class
"""
def inherits_from(obj, a_class):
        """Arg:
            obj - Object to be checked
            a_class - class to be evaluated
        Result:
            return True or False
        """
    return isinstance(obj, a_class) and type(obj) != a_class
