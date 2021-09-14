# https://www.hackerrank.com/challenges/pylons/problem
# !/bin/python3

def pylons(k, arr):
    count = i = 0
    loc = i + k - 1

    while i < len(arr):
        if arr[loc] == 1:
            i = loc + k
            loc = i + k - 1
            count += 1
            if loc >= n:
                loc = n - 1
        else:
            loc -= 1
            if loc < i - k + 1 or loc < 0:
                return -1

    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pylons(k, arr)
    print(result)
