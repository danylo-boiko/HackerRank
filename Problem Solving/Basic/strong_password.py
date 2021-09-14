# https://www.hackerrank.com/challenges/strong-password/problem
# !/bin/python3

def minimumNumber(n, password):
    count = 0
    if not any(char.isdigit() for char in password):
        count += 1
    if not any(char.islower() for char in password):
        count += 1
    if not any(char.isupper() for char in password):
        count += 1
    if not any(char in '!@#$%^&*()-+' for char in password):
        count += 1
    return max(count, 6 - n)


if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)
