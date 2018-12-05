#!/usr/bin/python3
import calculator_1 as op
if __name__ == "__main__":
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, op.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, op.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, op.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, op.div(a, b)))
