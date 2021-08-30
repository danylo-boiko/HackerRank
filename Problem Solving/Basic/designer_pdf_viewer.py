# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# !/bin/python3

def designerPdfViewer(h, word):
    height = 0

    for letter in word:
        height = max(height, h[ord(letter) - ord('a')])

    return height * len(word)

if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    print(result)
