# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# !/bin/python3

def hackerrankInString(s):
    target = "hackerrank"
    n = len(target)
    i = 0

    for char in s:
        if char == target[i]:
            i += 1
            if i == n:
                return "YES"

    return "NO"


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        print(result)
