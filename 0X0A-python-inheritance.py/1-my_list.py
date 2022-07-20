#!/usr/bin/python3
"""
contains the MyList class
"""

class MyList(list):
    """A subclass of a list"""
    def __init__(self):
        """Intializes the object"""
        super().__init__()
    

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))    

