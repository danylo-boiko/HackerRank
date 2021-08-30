# https://www.hackerrank.com/challenges/append-and-delete/problem
# !/bin/python3

def appendAndDelete(s, t, k):
    t_len = len(s) + len(t)
    cnt = 0

    for i, j in zip(s, t):
        if i == j:
            cnt += 1
        else:
            break

    if t_len < k or t_len <= 2 * cnt + k and t_len % 2 == k % 2:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
