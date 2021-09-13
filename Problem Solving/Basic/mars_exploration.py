# https://www.hackerrank.com/challenges/mars-exploration/problem
# !/bin/python3

def marsExploration(s):
    sos = list("SOS")
    count = 0

    for i in range(len(s)):
        if s[i] != sos[i % 3]:
            count += 1

    return count


if __name__ == '__main__':
    s = input()
    result = marsExploration(s)
    print(result)
