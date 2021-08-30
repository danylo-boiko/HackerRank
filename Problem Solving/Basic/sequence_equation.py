# https://www.hackerrank.com/challenges/permutation-equation/problem
# !/bin/python3

def permutationEquation(p):
    result = []

    for i in range(1, len(p) + 1):
        result.append(p.index(p.index(i) + 1) + 1)

    return result


if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    print('\n'.join(map(str, result)))
