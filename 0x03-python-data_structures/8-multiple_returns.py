def multiple_returns(sentence):
    length = len(sentence)
    first_ch = sentence[0]

    if length == None:
        first_ch = None

    tuple_a = (length, first_ch) 
    return(tuple_a)   