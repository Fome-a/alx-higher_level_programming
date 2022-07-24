#!/usr/bin/python3
"""
Contains subclass of class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Initialization of attributes """

    def __init__(self,width,height):
        super().__init__()
        self.__width = width
        self.__height = height
        
    def __str__(self):
        """Returns area of Rectangle"""
        return(f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """Returns area of triangle"""
        return (self.__width * self.__height)
        