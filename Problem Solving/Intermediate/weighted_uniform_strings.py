# !/bin/python3
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    temp = set()
    i = 0
    while i < len(s):
        j = i
        cur = 0
        while j < len(s) and s[j] == s[i]:
            cur += ord(s[j]) - ord('a') + 1
            temp.add(cur)
            j += 1
        i = j

    return ["Yes" if el in temp else "No" for el in queries]


if __name__ == '__main__':
    s = input()
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
