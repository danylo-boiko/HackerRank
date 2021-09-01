# https://www.hackerrank.com/challenges/missing-numbers/problem
# !/bin/python3

from collections import Counter


def missingNumbers(arr, brr):
    d1 = Counter(arr)
    d2 = Counter(brr)
    return sorted((d2 - d1).keys())


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    print(' '.join(map(str, result)))
