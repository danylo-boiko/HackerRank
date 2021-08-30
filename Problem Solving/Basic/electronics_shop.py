# https://www.hackerrank.com/challenges/electronics-shop/problem
# !/bin/python3

def getMoneySpent(keyboards, drives, b):
    maxAmount = -1

    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                maxAmount = max(maxAmount, keyboard + drive)

    return maxAmount


if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
