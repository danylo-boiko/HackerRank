# https://www.hackerrank.com/challenges/counting-valleys/problem
# !/bin/python3

def countingValleys(steps, path):
    valleyCount = level = 0
    d = {'U': 1, 'D': -1}

    for step in path:
        level += d[step]
        if level == 0 and step == 'U':
            valleyCount += 1

    return valleyCount


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
