# https://www.hackerrank.com/challenges/marcs-cakewalk/problem
# !/bin/python3

def marcsCakewalk(calorie):
    calorie = sorted(calorie, reverse=True)
    sum = 0

    for i in range(len(calorie)):
        sum += calorie[i] * 2 ** i

    return sum


if __name__ == '__main__':
    n = int(input().strip())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    print(result)
