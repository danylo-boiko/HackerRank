# https://www.hackerrank.com/challenges/circular-array-rotation/problem
# !/bin/python3

def circularArrayRotation(a, k, queries):
    result = []
    k = k % len(a)

    for q in queries:
        result.append(a[(n - k + q) % n])

    return result


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    q = int(first_multiple_input[2])
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = circularArrayRotation(a, k, queries)
    print('\n'.join(map(str, result)))
