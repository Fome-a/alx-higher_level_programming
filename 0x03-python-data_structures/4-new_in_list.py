#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    new_list[idx] = element

    if idx < 0:
        return(new_list)

    length = len(my_list)

    if idx < length - 1:
        return(new_list)

    return(new_list)
