#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Count = len(sys.argv)

    if Count == 0:
        print("0 arguments")
    elif Count == 1:
        print("1 argument:")
        print("1 : {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(Count))
        for i in range(1, Count):
            print("{:d} : {:s}". format(i, sys.argv[i]))
