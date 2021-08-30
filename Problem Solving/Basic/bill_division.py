# https://www.hackerrank.com/challenges/bon-appetit/problem
# !/bin/python3

def bonAppetit(bill, k, b):
    s = sum(bill)
    changes = (s - bill[k]) // 2

    if b == changes:
        print("Bon Appetit")
    else:
        print(b - changes)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
