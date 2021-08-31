# https://www.hackerrank.com/challenges/pangrams/problem
# !/bin/python3

def pangrams(s):
    if len(set(s.lower()) - set(' ')) == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
