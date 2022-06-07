#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_ch = sentence[0]

    if length is None:
<<<<<<< HEAD
        tuple_a = (length,None)
=======
        tuple_a = (length, None)
>>>>>>> 9d409bbed6ee78e62c71afd41e933ffb7ef97a63
    else:
        tuple_a = (length, first_ch)
    return(tuple_a)
