# https://www.hackerrank.com/challenges/fibonacci-modified/problem
# !/bin/python3

def fibonacciModified(t1, t2, n):
    for i in range(n - 1):
        t1, t2 = t2, t1 + t2 ** 2

    return t1


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    t1 = int(first_multiple_input[0])
    t2 = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    result = fibonacciModified(t1, t2, n)
    print(result)
