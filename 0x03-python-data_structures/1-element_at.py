#!/usr/bin/python3
def element_at(my_list, idx):
    b = len(my_list)
    c = my_list[idx]
    if idx < 0:
        return (None)
    if idx > b:
        return (None)

    return (c)
