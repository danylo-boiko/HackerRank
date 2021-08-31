# https://www.hackerrank.com/challenges/chocolate-feast/problem
# !/bin/python3

def chocolateFeast(n, c, m):
    eatenBars = n // c
    wrappers = eatenBars

    while wrappers >= m:
        newBars = wrappers // m
        eatenBars += newBars
        wrappers = wrappers % m + newBars

    return eatenBars


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        result = chocolateFeast(n, c, m)
        print(result)
