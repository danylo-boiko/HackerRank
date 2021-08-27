# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# !/bin/python3

def birthdayCakeCandles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(str(result) + '\n')
