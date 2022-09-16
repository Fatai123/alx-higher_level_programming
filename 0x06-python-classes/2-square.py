#!/usr/bin/python3
class Square:
    """ To define a square
        Private instance attribute: size
        Instantiation with size (no type/value verification)
    """
    def __init__(self, size=0):
        """Initialize the size and verify the type and value"""
        if not isinstance(size, int):
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
