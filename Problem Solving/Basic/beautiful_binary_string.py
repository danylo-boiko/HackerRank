# https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# !/bin/python3

def beautifulBinaryString(b):
    b = list(b)
    count = 0

    for i in range(1, len(b) - 1):
        if b[i - 1] == '0' and b[i] == '1' and b[i + 1] == '0':
            b[i + 1] = '1'
            count += 1

    return count


if __name__ == '__main__':
    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)
    print(result)
