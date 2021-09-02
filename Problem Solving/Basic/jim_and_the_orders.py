# https://www.hackerrank.com/challenges/jim-and-the-orders/problem
# !/bin/python3

def jimOrders(orders):
    tuples = []
    i = 1

    for order in orders:
        tuples.append((order[0] + order[1], i))
        i += 1

    tuples.sort(key=lambda x: x[0])
    return [x[1] for x in tuples]


if __name__ == '__main__':
    n = int(input().strip())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
    result = jimOrders(orders)
    print(' '.join(map(str, result)))
