# https://www.hackerrank.com/challenges/angry-professor/problem
# !/bin/python3

def angryProfessor(k, a):
    count = 0

    for el in a:
        if el <= 0:
            count += 1

    if count < k:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k, a)
        print(result)
