#!/usr/bin/python3
"""
Read file function
"""


def read_file(filename=""):
    """The read file function"""

    with open(filename, encoding="utf-8") as myfile:
        for line in myfile:
            print(myfile.read())
