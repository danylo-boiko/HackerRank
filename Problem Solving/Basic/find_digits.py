# https://www.hackerrank.com/challenges/find-digits/problem
# !/bin/python3

def findDigits(n):
    count = 0
    for digit in str(n):
        num = int(digit)
        if num != 0 and n % num == 0:
            count += 1
    return count


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
