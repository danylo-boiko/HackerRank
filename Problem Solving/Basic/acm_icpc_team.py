# https://www.hackerrank.com/challenges/acm-icpc-team/problem
# !/bin/python3

def acmTeam(topic):
    count = maxSub = 0

    for i in range(n):
        for j in range(i, n):
            sub = 0
            for x, y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    sub += 1

            if sub > maxSub:
                maxSub = sub
                count = 1
            elif sub == maxSub:
                count += 1

    return maxSub, count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    print('\n'.join(map(str, result)))
