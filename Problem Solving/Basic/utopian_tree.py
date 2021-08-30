# https://www.hackerrank.com/challenges/utopian-tree/problem
# !/bin/python3

def utopianTree(n):
    s = 0

    for i in range(n + 1):
        s = s + 1 if i % 2 == 0 else s * 2

    return s


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
