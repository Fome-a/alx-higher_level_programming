def safe_print_list(my_list=[], x=0):
    cpt = 1
    try:
        for n in my_list:
            if cpt <= x:
                print(n, end="")
                cpt += 1
        print("")
        return(cpt - 1)
    except Exception:
        return(0)
    pass
