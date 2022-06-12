#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    for k in a_dictionary.keys():
        new_dir[k] = a_dictionary[k] * 2
    return(new_dir)
