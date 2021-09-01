# https://www.hackerrank.com/challenges/gem-stones/problem
# !/bin/python3

def gemstones(arr):
    intersect = set(arr[0])

    for i in range(1, len(arr)):
        intersect = intersect.intersection(set(arr[i]))

    return len(intersect)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)
