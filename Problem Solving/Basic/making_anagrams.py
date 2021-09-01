# https://www.hackerrank.com/challenges/making-anagrams/problem
# !/bin/python3

from collections import Counter


def makingAnagrams(s1, s2):
    d1 = Counter(s1)
    d2 = Counter(s2)
    total = (d1 - d2) + (d2 - d1)

    return sum(total.values())


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    print(result)
