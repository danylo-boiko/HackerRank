# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# !/bin/python3

def theLoveLetterMystery(s):
    count = 0
    n = len(s)

    for i in range(n // 2):
        count += abs(ord(s[i]) - ord(s[n - i - 1]))

    return count


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        print(result)
