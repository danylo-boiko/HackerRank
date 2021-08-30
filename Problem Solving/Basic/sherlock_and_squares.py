# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
# !/bin/python3

from math import floor, sqrt, ceil


def squares(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        print(result)
