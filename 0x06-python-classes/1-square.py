#!/usr/bin/python3
class Square:
    '''To define a square
            Private instance attribute: size
            Instantiation with size (no type/value verification)
    '''
    def __init__(self, size):
        '''Initialize the size'''
        self.__size = size
