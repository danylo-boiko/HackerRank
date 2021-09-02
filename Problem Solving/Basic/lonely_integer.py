# https://www.hackerrank.com/challenges/lonely-integer/problem
# !/bin/python3

def lonelyinteger(a):
    res = 0

    for el in a:
        res ^= el

    return res


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    print(result)
