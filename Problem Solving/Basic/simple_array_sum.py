# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(str(result) + '\n')
