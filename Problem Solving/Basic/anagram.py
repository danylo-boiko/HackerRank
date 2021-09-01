# https://www.hackerrank.com/challenges/anagram/problem
# !/bin/python3

from collections import Counter


def anagram(s):
    n = len(s)

    if n % 2 == 1:
        return -1

    s = Counter(s[:n // 2]) - Counter(s[n // 2:])

    return sum(s.values())


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        print(result)
