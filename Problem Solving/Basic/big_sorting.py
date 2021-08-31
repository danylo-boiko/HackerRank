# https://www.hackerrank.com/challenges/big-sorting/problem
# !/bin/python3

def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted


if __name__ == '__main__':
    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    result = bigSorting(unsorted)
    print('\n'.join(result))
