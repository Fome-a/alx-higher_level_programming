#!/usr/bin/python3
"""Creating a rectangle class subclass of Base"""
Base = __import__('base').Base
class Rectangle(Base):
    def __init__(self,width,height,x=0,y=0,id=None):
        """Initializing the class rectangle"""
        super().__init__(self,id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width
    @width.setter
    def width(self,value):
        """Setting the width of the rectangle"""
        if value != int:
            raise TypeError("Value must be an int")
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        self.__width = value
    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height
    @height.setter
    def height(self,value):
        """Setting the height of the rectangle"""
        if value != int:
            raise TypeError("Value must be an int")
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        self.__height = value
    @property
    def x(self):
        """Value x"""
        return self.__x
    @x.setter
    def x(self,value):
        """Setting the value x"""
        if value != int:
            raise TypeError("Value must be an int")
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        self.__x = value
    @property
    def y(self):
        """Value y"""
        return self.__y
    @y.setter
    def width(self,value):
        """Setting the value of y"""
        if value != int:
            raise TypeError("Value must be an int")
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        self.__y = value
