import sys, numpy as np


def factorial(n):
    result = 1
    for i in np.arange(1, n, 1):
        result += (result*i)
    return result


def usage():
    print "\t\tIncorrect Usage!"
    print "Usage: python factorial.py <Integer>"


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        print factorial(int(sys.argv[1]))


if __name__ == '__main__':
    main()
