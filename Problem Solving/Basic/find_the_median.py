# https://www.hackerrank.com/challenges/find-the-median/problem
# !/bin/python3

def findMedian(arr):
    return sorted(arr)[len(arr) // 2 + len(arr) % 2 - 1]


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    print(result)
