# https://www.hackerrank.com/challenges/migratory-birds/problem
# !/bin/python3

def migratoryBirds(arr):
    l = [0] * len(arr)

    for i in range(len(arr)):
        l[arr[i]] += 1

    return l.index(max(l))

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
