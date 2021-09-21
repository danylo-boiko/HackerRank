# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
# !/bin/python3

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    i = len(sticks) - 3
    while i >= 0 and sticks[i] + sticks[i + 1] <= sticks[i + 2]:
        i -= 1

    if i >= 0:
        return sticks[i: i + 3]
    else:
        return [-1]


if __name__ == '__main__':
    n = int(input().strip())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    print(' '.join(map(str, result)))
