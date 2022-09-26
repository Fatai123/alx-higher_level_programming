#!/usr/bin/python3
class MyList(list):
    """Class MyList inherits from list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print("{}".format(sorted(self[:])))
