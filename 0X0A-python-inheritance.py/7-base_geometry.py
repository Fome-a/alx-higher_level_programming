#!/usr/bin/python3
"""Contains the class BaseGeometry"""


class BaseGeometry:
    """Base Geometry class with 2 public instances
    """  
    def area(self):
        """raise an exception when called"""
        raise Exception("area() is not implemented")
    def integer_validator(self,name,value):
        """validates value"""
        type(name) == str
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))