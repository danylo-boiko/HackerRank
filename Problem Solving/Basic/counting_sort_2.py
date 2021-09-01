# https://www.hackerrank.com/challenges/countingsort2/problem
# !/bin/python3

def countingSort(arr):
    count = [0] * (max(arr) + 1)
    for num in arr:
        count[num] += 1

    sortedArr = []
    for i in range(len(count)):
        while count[i] != 0:
            count[i] -= 1
            sortedArr.append(i)

    return sortedArr


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(' '.join(map(str, result)))
