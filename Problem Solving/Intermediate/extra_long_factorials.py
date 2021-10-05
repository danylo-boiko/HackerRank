# https://www.hackerrank.com/challenges/extra-long-factorials/problem
# !/bin/python3

from math import prod


def extraLongFactorials(n):
    return prod(range(2, n + 1))


if __name__ == '__main__':
    n = int(input().strip())
    print(extraLongFactorials(n))
