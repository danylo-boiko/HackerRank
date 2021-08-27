# https://www.hackerrank.com/challenges/a-very-big-sum/problem
# !/bin/python3

def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(str(result) + '\n')
