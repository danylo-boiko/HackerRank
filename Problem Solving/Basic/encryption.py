# https://www.hackerrank.com/challenges/encryption/problem
# !/bin/python3

import math


def encryption(s):
    s = s.replace(" ", "")
    c = math.ceil(math.sqrt(len(s)))
    return " ".join([s[i::c] for i in range(c)])


if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)
