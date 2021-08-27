# https://www.hackerrank.com/challenges/staircase/problem
# !/bin/python3

def staircase(n):
    for i in range(1, n + 1):
        s = '#' * i
        print(s.rjust(n))


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
