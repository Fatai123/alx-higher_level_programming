#!/usr/bin/python3
"""check if the object is an instance of, or if the object is an 
   instance of a class that inherited from, the specified class
"""
def is_kind_of_class(obj, a_class):
    """Arg:
            obj - Object to be checked
            a_class - class to be estimated

        Result:
            return True or False
    """
    return isinstance(obj, a_class)
