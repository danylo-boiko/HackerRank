# https://www.hackerrank.com/challenges/countingsort4/problem
# !/bin/python3

def countSort(arr):
    result = [[] for i in range(100)]

    for i in range(len(arr) // 2):
        result[int(arr[i][0])].append('-')

    for i in range(len(arr) // 2, len(arr)):
        result[int(arr[i][0])].append(arr[i][1])

    for string in result:
        if string:
            print(*string, end=' ')


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)
