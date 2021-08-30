# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# !/bin/python3

from collections import Counter


def cutTheSticks(arr):
    result = list()
    n = len(arr)
    s = Counter(arr)

    for i in sorted(s.keys()):
        result.append(n)
        n -= s[i]

    return result


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    print('\n'.join(map(str, result)))
