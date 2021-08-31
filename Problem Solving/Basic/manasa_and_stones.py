# https://www.hackerrank.com/challenges/manasa-and-stones/problem
# !/bin/python3

def stones(n, a, b):
    result = set()

    for i in range(1, n + 1):
        result.add(a * (n - i) + b * (i - 1))

    return sorted(result)


if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print(' '.join(map(str, result)))
