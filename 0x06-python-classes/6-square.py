#!/usr/bin/python3
class Square:
    """ To define a square
        Private instance attribute: size
        Instantiation with size (no type/value verification)
    """
    def __init__(self, size=0, position =(0,0)):
        """Initialize the size and position"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """To set position to value and verify"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        print(self.__size * self.__size)

    def my_print(self):
        """Print in stdout the square with the character #,
            at a given position"""
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
