# https://www.hackerrank.com/challenges/two-characters/problem
# !/bin/python3

def validate(line):
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            return False
    return True


def alternate(s):
    st = list(set(s))
    mx_len = 0
    for i in range(len(st)):
        for j in range(i + 1, len(st)):
            cpy = [c for c in s if c == st[i] or c == st[j]]
            if validate(cpy):
                mx_len = max(mx_len, len(cpy))

    return mx_len


if __name__ == '__main__':
    l = int(input().strip())
    s = input()
    result = alternate(s)
    print(result)
