#!/usr/bin/python3
def element_at(my_list, idx):
    b = len(my_list)
    c = my_list[idx]
    if idx < 0:
        print("None")
    if idx > b:
            print("None")
    else:
        return c
