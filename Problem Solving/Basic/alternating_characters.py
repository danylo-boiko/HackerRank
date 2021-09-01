# https://www.hackerrank.com/challenges/alternating-characters/problem
# !/bin/python3

def alternatingCharacters(s):
    count = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1

    return count


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)
