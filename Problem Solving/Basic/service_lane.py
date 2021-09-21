# https://www.hackerrank.com/challenges/service-lane/problem
# !/bin/python3

def serviceLane(cases, width):
    return [min(width[start: stop + 1]) for start, stop in cases]


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    result = serviceLane(cases, width)
    print('\n'.join(map(str, result)))
