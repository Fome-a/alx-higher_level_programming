#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv) - 1
    if length > 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = sys.argv[1]
    b = sys.argv[3]

    from calculator_1 import add, sub, mul, div
    if operator == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if operator == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if operator == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if operator == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
