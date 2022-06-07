#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_a = len(tuple_a)
    new_b = len(tuple_b)

    if new_a == 0:
        a0 = 0
        a1 = 0
    elif new_a == 1:
        a0 = tuple_a[0]
        tuple_a[1] = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if new_b == 0:
        b0 = 0
        b1 = 0
    elif new_b == 1:
        b0 = tuple_b[0]
        b1 = 1
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    add1_tuple = a0 + b0
    add2_tuple = a1 + b1

    new_tuple = (add1_tuple, add2_tuple)
    return(new_tuple)
