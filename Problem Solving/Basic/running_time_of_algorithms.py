# https://www.hackerrank.com/challenges/runningtime/problem
# !/bin/python3

def runningTime(arr):
    shifts = 0

    for j in range(1, n):
        key = arr[j]
        i = j
        while i > 0 and arr[i - 1] > key:
            arr[i] = arr[i - 1]
            shifts += 1
            i -= 1
        arr[i] = key

    return shifts


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    print(result)
