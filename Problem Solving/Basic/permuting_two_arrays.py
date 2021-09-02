# https://www.hackerrank.com/challenges/two-arrays/problem
# !/bin/python3

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        if a + b < k:
            return "NO"

    return "YES"


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        print(result)
