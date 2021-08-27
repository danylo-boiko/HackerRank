# https://www.hackerrank.com/challenges/diagonal-difference/problem
# !/bin/python3

def diagonalDifference(arr):
    leftDiag = rightDiag = 0
    for i in range(len(arr)):
        leftDiag += arr[i][i]
        rightDiag += arr[i][len(arr) - i - 1]
    return abs(leftDiag - rightDiag)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(str(result) + '\n')
