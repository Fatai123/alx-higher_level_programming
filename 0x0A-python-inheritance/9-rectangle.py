#!/usr/bin/python3
"""To create a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
    
    def __str__(self):
        """Return the rectangle details"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):

        """overide the area instance method in BaseGeometry
           to return area of the rectangle (area implemented)
        """
        return self.__width * self.__height
