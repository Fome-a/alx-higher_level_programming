#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy
    lists_1 = new_dict.values()
    for i in lists_1:
        result = lists_1[i] * 2
    return(result)
