# https://www.hackerrank.com/challenges/an-interesting-game-1/problem
# !/bin/python3

def gamingArray(arr):
    mx = count = 0

    for el in arr:
        if el > mx:
            mx = el
            count += 1

    return "ANDY" if count % 2 == 0 else "BOB"


if __name__ == '__main__':
    g = int(input().strip())
    for g_itr in range(g):
        arr_count = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = gamingArray(arr)
        print(result)
