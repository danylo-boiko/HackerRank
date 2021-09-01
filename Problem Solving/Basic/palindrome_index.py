# https://www.hackerrank.com/challenges/palindrome-index/problem
# !/bin/python3

def palindromeIndex(s):
    if s == s[::-1]:
        return -1

    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if s[i:n - i - 1] == s[i: n - i - 1][::-1]:
                return n - i - 1
            elif s[i + 1:n - i] == s[i + 1:n - i][::-1]:
                return i

    return -1


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)
