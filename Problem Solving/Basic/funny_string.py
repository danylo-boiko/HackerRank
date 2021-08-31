# https://www.hackerrank.com/challenges/funny-string/problem
# !/bin/python3

def funnyString(s):
    rev = s[::-1]

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(rev[i]) - ord(rev[i - 1])):
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        print(result)
