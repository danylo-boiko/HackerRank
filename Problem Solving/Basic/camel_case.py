# https://www.hackerrank.com/challenges/camelcase/problem
# !/bin/python3

def camelcase(s):
    count = 1

    for char in s:
        if char.isupper():
            count += 1

    return count


if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)
