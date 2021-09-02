# https://www.hackerrank.com/challenges/mark-and-toys/problem
# !/bin/python3

def maximumToys(prices, k):
    toys = total = 0
    prices.sort()

    for el in prices:
        if el + total <= k:
            toys += 1
            total += el

    return toys


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)
