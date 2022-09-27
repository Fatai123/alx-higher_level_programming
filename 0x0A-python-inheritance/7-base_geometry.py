#!/usr/bin/python
"""classs with public instance method"""
class BaseGeometry:
    """To raise an Execption with message"""

    def area(self):
        raise Exception("area() is not implemented")

    """To validate the value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
