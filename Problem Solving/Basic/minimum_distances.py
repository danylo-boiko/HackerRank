# https://www.hackerrank.com/challenges/minimum-distances/problem
# !/bin/python3

def minimumDistances(a):
    distance = len(a)

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                distance = min(distance, j - i)

    return -1 if distance == len(a) else distance


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    print(result)
