# https://www.hackerrank.com/challenges/tutorial-intro/problem
# !/bin/python3

def introTutorial(V, arr):
    return arr.index(V)


if __name__ == '__main__':
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(V, arr)
    print(result)
