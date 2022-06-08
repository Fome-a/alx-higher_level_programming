import sys
if __name__ == "__main__":
    operator = sys.argv[2]
    length = len(sys.argv) - 1
    if length > 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        from calculator_1 import add, sub, mul, div
        a = sys.argv[1]
        b = sys.argv[3]

        if operator == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
