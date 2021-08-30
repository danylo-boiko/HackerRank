# https://www.hackerrank.com/challenges/sock-merchant/problem
# !/bin/python3

def sockMerchant(n, ar):
    cnt = 0
    d = {}

    for el in ar:
        d[el] = d.get(el, 0) + 1

    for k in d.keys():
        cnt += d[k] // 2

    return cnt

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
