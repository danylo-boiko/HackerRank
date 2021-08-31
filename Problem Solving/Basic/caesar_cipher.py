# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
# !/bin/python3

def caesarCipher(s, k):
    result = list()

    for i in range(len(s)):
        if s[i].isalpha():
            char = 'A' if s[i].isupper() else 'a'
            result.append(chr(ord(char) + ((ord(s[i]) - ord(char) + k) % 26)))
        else:
            result.append(s[i])

    return "".join(result)


if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
