# https://www.hackerrank.com/challenges/fair-rations/problem
# !/bin/python3

def fairRations(B):
    breads = 0
    n = len(B)

    for i in range(n - 1):
        if B[i] % 2 == 1:
            breads += 2
            B[i + 1] += 1

    if B[n - 1] % 2 == 1:
        return "NO"
    else:
        return breads


if __name__ == '__main__':
    N = int(input().strip())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)
    print(result)
