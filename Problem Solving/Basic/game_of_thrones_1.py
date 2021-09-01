# https://www.hackerrank.com/challenges/game-of-thrones/problem
# !/bin/python3

from collections import Counter


def gameOfThrones(s):
    s = Counter(s)
    count = 0

    for k, v in s.items():
        count += v % 2

    return "NO" if count > 1 else "YES"


if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
    print(result)
