#!/usr/bin/python3
import sys
import calculator_1 as calc
if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    o = sys.argv[2]
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    elif o == '+':
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif o == '-':
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif o == '*':
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif o == '/':
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /".format())
        sys.exit(1)
