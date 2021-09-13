# https://www.hackerrank.com/challenges/quicksort1/problem
# !/bin/python3

def quickSort(arr):
    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return [*left, pivot, *right]


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    print(' '.join(map(str, result)))
