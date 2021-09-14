# https://www.hackerrank.com/challenges/candies/problem
# !/bin/python3

def candies(n, arr):
    dp = [1] * n

    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            dp[i] = dp[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1] and dp[i] <= dp[i + 1]:
            dp[i] = dp[i + 1] + 1

    return sum(dp)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = candies(n, arr)
    print(result)
