#!/usr/bin/python3
"""Creating a base class"""

class Base:
    """defining class attribute"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initializing class base """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        