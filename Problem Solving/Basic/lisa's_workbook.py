# https://www.hackerrank.com/challenges/lisa-workbook/problem
# !/bin/python3

def workbook(n, k, arr):
    page = 1
    count = 0

    for probs in arr:
        for idx in range(1, probs + 1):
            if idx == page:
                count += 1
            if idx == probs or idx % k == 0:
                page += 1

    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)
