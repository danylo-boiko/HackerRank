# https://www.hackerrank.com/challenges/equality-in-a-array/problem
# !/bin/python3

from collections import Counter


def equalizeArray(arr):
    return len(arr) - max(Counter(arr).values())


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    print(result)
