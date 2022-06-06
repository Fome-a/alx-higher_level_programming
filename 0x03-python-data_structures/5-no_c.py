#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    for i in new_string:
        if ('c') or ('C') in new_string:
            return(new_string.translate({ord('c'): None, ord('C'): None}))
