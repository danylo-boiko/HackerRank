# https://www.hackerrank.com/challenges/tower-breakers-1/problem
# !/bin/python3


def towerBreakers(n, m):
    return 2 if m == 1 or n % 2 == 0 else 1


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = towerBreakers(n, m)
        print(result)
