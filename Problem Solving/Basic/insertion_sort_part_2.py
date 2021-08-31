# https://www.hackerrank.com/challenges/insertionsort2/problem
# !/bin/python3

def insertionSort2(n, arr):
    for j in range(1, n):
        key = arr[j]
        i = j
        while i > 0 and arr[i - 1] > key:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = key
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)
