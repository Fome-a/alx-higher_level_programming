#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if ('c') or ('C') in my_string:
            return(my_string.translate({ord('c'): None, ord('C'): None}))
