# https://www.hackerrank.com/challenges/strange-advertising/problem
# !/bin/python3

def viralAdvertising(n):
    likes = 0
    shared = 5

    for i in range(n):
        like = shared // 2
        likes += like
        shared = like * 3

    return likes


if __name__ == '__main__':
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
