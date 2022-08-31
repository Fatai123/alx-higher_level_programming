#!/usr/bin/python3
def no_c(my_string):
    split_string = list(my_string)
    for letter in split_string:
        if letter == "c" or letter == "C":
            split_string.remove(letter)
    new_string = ''.join(split_string)
    return new_string
