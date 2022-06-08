#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    index = 1
    Count = len(argv)

    if Count == 0:
        print("{} arguments".format(Count))
    elif Count == 1:
        print("{:d} argument:".format(Count))
        print("{:d} : {:s}".format(index, sys.argv[1]))
    else:
        print("{} argument:".format(Count))
        while index <= Count:
            print("{:d} : {:s}". format(index, sys.argv[index]))
            index += 1
