# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
# !/bin/python3

def minimumAbsoluteDifference(arr):
    diffs = []
    arr.sort()
    for i in range(len(arr) - 1):
        diffs.append(abs(arr[i] - arr[i + 1]))
    return min(diffs)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
