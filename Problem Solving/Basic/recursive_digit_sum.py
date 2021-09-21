# https://www.hackerrank.com/challenges/recursive-digit-sum/problem
# !/bin/python3

def superDigit(n, k):
    x = int(n) * k % 9
    return x if x else 9


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    print(result)
