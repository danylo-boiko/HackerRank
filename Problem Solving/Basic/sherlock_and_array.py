# https://www.hackerrank.com/challenges/sherlock-and-array/problem
# !/bin/python3

def balancedSums(arr):
    right = sum(arr)
    left = 0

    for num in arr:
        if 2 * left == right - num:
            return "YES"
        left += num

    return "NO"


if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        print(result)
