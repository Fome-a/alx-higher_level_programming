#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes with area function
"""


class Square:
    def __init__(self, size=0):
        """Constructor of a Square with the size"""
        self.size = size

    @property
    def size(self):
        """Getter of the private attribute size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for the size private attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public method returns the square of size"""
        return (self.__size ** 2)
