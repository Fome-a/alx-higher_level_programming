#!/usr/bin/python3
"""Creating a class a subclass of Rectangle"""
"""imports class Rectangle from module rectangle.py in the file models"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Definnig Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=0, y=0, id=None)
    
    @property
    def size(self):
        """Getting size of square"""
        return self.width
    @size.setter
    def size(self,value):
        """Setting size of square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Method returns formatted output"""
        return "[Square] ({}) {:d}/{:d} - {:d}" .format(self.id,self.x,self.y,self.width)
    
    def update(self, *args, **kwargs):
        if len(args) != 0:
            self.id = args[0]
            self.size= args[1]
            self.x= args[2]
            self.y=args[3]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self,key,value)

    def to_dictionary(self):
        """Returning dictionary representation of square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        