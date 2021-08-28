# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# !/bin/python3

def breakingRecords(scores):
    minCount = maxCount = 0
    minScore = maxScore = scores[0]
    for i in range(1, len(scores)):
        if minScore < scores[i]:
            minScore = scores[i]
            minCount += 1
        elif maxScore > scores[i]:
            maxScore = scores[i]
            maxCount += 1
    return minCount, maxCount

if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
