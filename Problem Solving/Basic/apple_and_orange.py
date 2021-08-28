# https://www.hackerrank.com/challenges/apple-and-orange/problem
# !/bin/python3


def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(len([el + a for el in apples if el + a in range(s, t + 1)]))
    print(len([el + b for el in oranges if el + b in range(s, t + 1)]))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
