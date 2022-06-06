def multiple_returns(sentence):
    length = len(sentence)
    first_ch = sentence[0]

    if length is None:
        tuple_a = (length, None)
    else:
        tuple_a = (length, first_ch)
    return(tuple_a)
