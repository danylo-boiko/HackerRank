# https://www.hackerrank.com/challenges/happy-ladybugs/problem
# !/bin/python3

def happyLadybugs(b):
    for a in set(b):
        if a != '_' and b.count(a) == 1:
            return "NO"

    if b.count('_') == 0:
        for i in range(1, len(b) - 1):
            if b[i - 1] != b[i] and b[i + 1] != b[i]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)
        print(result)
