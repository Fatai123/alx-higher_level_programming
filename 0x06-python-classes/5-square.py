#!/usr/bin/python3
class Square:
    """ To define a square
        Private instance attribute: size
        Instantiation with size (no type/value verification)
    """
    def __init__(self, size=0):
        """Initialize the size"""
        self.__size = size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set size to value and verify """
        if not isinstance(value, int):
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area"""
        return self.__size * self.__size

    def my_print(self):
        """Print in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end=' ')
                print()
