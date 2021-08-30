# https://www.hackerrank.com/challenges/picking-numbers/problem
# !/bin/python3

def pickingNumbers(a):
    maxCount = 0

    for el in a:
        maxCount = max(maxCount, a.count(el) + a.count(el - 1))

    return maxCount


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)
