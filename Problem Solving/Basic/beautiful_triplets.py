# https://www.hackerrank.com/challenges/beautiful-triplets/problem
# !/bin/python3

from collections import Counter


def beautifulTriplets(d, arr):
    m = Counter(arr)
    count = 0

    for num in arr:
        if m[num + d] and m[num + d + d]:
            count += 1

    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print(result)
