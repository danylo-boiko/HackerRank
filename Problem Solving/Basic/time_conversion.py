# https://www.hackerrank.com/challenges/time-conversion/problem
# !/bin/python3

def timeConversion(s):
    meridian = s[-2:]
    if meridian == 'PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    if meridian == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    return s[:-2]


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
