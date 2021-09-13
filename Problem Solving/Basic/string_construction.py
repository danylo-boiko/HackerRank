# https://www.hackerrank.com/challenges/string-construction/problem
# !/bin/python3

def stringConstruction(s):
    return len(set(s))


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        print(result)
