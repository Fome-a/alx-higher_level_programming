#!/usr/bin/python3
"""
Contains function check of obj class type
"""
def is_same_class(obj, a_class):
    """function that returns bool """
    x = (type(obj) == a_class)
    return x