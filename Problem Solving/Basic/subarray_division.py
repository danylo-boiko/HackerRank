# https://www.hackerrank.com/challenges/the-birthday-bar/problem
# !/bin/python3

def birthday(s, d, m):
    count = 0
    total = sum(s[:m])

    if total == d:
        count += 1

    # sliding
    for i in range(m, len(s)):
        total += s[i]
        total -= s[i - m]
        if total == d:
            count += 1

    return count


if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    print(result)
