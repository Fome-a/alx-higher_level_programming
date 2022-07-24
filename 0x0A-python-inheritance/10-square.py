#!/usr/bin/python3
"""
Contains subclass
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Starts intialization"""
    def __init__(self,size):
        super().__init__(size,size)
        self.integer_invalidator = ("size",size)
        self.__size = size
