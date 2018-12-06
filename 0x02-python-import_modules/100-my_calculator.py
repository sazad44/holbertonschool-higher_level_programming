#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        o = sys.argv[2]
    if o == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif o == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif o == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif o == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /".format())
        sys.exit(1)
