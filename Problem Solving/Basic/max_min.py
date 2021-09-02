# https://www.hackerrank.com/challenges/angry-children/problem
# !/bin/python3

def maxMin(k, arr):
    arr.sort()
    return min([arr[i + k - 1] - arr[i] for i in range(n - k + 1)])


if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    print(result)
