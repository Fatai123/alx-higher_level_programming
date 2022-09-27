#!/usr/bin/python3
"""classs with public instance method"""
class BaseGeometry:
    """To raise an Execption with message"""

    def area(self):
        raise Exception("area() is not implemented")

    """To validate the value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

"""class Rectangle that inherits from BaseGeometry"""
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
    
    """Private instance attribute

       Arg:
            - width: width of the rectangle
            - height: height of the rectangle

       To be verify with integer_validator (inherted instance method)
    """
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height
