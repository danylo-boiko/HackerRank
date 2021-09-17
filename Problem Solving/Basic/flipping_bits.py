# https://www.hackerrank.com/challenges/flipping-bits/problem
# !/bin/python3


def flippingBits(n):
    return 2 ** 32 - 1 - n


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print(result)
