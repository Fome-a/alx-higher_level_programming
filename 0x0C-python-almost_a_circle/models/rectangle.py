#!/usr/bin/python3
"""Creating a rectangle class subclass of Base"""
from models.base import Base
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
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value
    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height
    @height.setter
    def height(self,value):
        """Setting the height of the rectangle"""
        if value != int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value
    @property
    def x(self):
        """Value x"""
        return self.__x
    @x.setter
    def x(self,value):
        """Setting the value x"""
        if value != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        """Value y"""
        return self.__y
    @y.setter
    def width(self,value):
        """Setting the value of y"""
        if value != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """public method returns area of rectangle"""
        return self.width * self.height
    def display(self):
        """print ing the rectangle in stdout"""
        for counter in range(self.y):
            print(' ')
        for counts in range(self.height):
            print(' ' * self.x + '#' * self.width)
    
    def __str__(self):
        """method returns formatted display information"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format (self.id, self.x,self.y,self.width,self.height)
    
    def update(self, *args, **kwargs):
        """Updating rectangle attributes"""
        if len(args) != 0:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self,key,value)
    
    def to_dictionary(self):
        """Method returns dictionary representation"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
