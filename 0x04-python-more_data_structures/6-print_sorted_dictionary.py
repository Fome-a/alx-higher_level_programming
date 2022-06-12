#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = a_dictionary.keys()
    sorted_keys = sorted(list_keys)
    for key in list_keys:
        print(key, ':', a_dictionary[key])
