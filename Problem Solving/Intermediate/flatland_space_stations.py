# https://www.hackerrank.com/challenges/flatland-space-stations/problem
# !/bin/python3

def flatlandSpaceStations(n, c):
    c.sort()
    max_gap = 0

    if len(c) > 1:
        for a, b in zip(c[1:], c):
            max_gap = max(max_gap, a - b)

    return max(max_gap // 2, c[0], n - c[-1] - 1)


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    print(result)
