# https://www.hackerrank.com/challenges/mini-max-sum/problem
# !/bin/python3


def miniMaxSum(arr):
    print(sum(arr) - min(arr), sum(arr) - max(arr))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
