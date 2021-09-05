# https://www.hackerrank.com/challenges/greedy-florist/problem
# !/bin/python3

def getMinimumCost(k, c):
    cost = 0
    m = 1

    c.sort(reverse=True)

    for i in range(len(c)):
        cost += c[i] * m
        if (i + 1) % k == 0:
            m += 1

    return cost


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
