# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# !/bin/python3

from collections import Counter


def isValid(s):
    cnt = Counter(s)

    if len(set(cnt.values())) == 1:
        return "YES"
    elif len(set(cnt.values())) == 2:
        for k in cnt:
            cnt[k] -= 1
            temp = list(cnt.values())
            if 0 in temp:
                temp.remove(0)
            if len(set(temp)) == 1:
                return "YES"
            else:
                cnt[k] += 1

        return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)
