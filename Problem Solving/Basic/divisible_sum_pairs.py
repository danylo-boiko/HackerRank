# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# !/bin/python3

def divisibleSumPairs(n, k, ar):
    cnt = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                cnt += 1

    return cnt

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    print(result)
