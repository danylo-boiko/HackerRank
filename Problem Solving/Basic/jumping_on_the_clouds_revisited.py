# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# !/bin/python3

def jumpingOnClouds(c, k):
    energy = 100

    i = 0
    while True:
        energy = energy - 1 - 2 * c[i]
        i = (i + k) % len(c)
        if i == 0:
            break

    return energy


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    print(result)
