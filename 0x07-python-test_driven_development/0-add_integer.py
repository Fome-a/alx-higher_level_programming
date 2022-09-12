#!/usr/bin/python3
"""A function that adds two integers."""


def add_integer(a, b=98):
    """ Given two integers,return sum"""
    if isinstance (a, float):
        a = int(a)
    if isinstance (b, float):
        b = int(b)
    if type(a) is not int: 
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
