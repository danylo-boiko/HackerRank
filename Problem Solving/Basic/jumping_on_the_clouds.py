# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# !/bin/python3

def jumpingOnClouds(c):
    i = jumps = 0

    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            jumps += 1
            i += 2
        elif i + 1 < n and c[i + 1] == 0:
            jumps += 1
            i += 1

    return jumps


if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
