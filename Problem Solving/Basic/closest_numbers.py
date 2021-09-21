# https://www.hackerrank.com/challenges/closest-numbers/problem
# !/bin/python3

def closestNumbers(arr):
    arr.sort()
    ans = []
    mn = arr[len(arr) - 1]
    for i in range(len(arr) - 1):
        mn = min(arr[i + 1] - arr[i], mn)

    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == mn:
            ans.extend([arr[i], arr[i + 1]])

    return ans


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(' '.join(map(str, result)))
