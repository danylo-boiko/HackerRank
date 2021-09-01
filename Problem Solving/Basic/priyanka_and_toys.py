# https://www.hackerrank.com/challenges/priyanka-and-toys/problem
# !/bin/python3

def toys(w):
    w.sort()
    containers = 1
    max_weight = w[0] + 4

    for weight in w:
        if weight > max_weight:
            containers += 1
            max_weight = weight + 4

    return containers


if __name__ == '__main__':
    n = int(input().strip())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(result)
