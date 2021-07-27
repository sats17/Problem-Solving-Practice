"""
Problem Link -
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

Script description -
When you select a contiguous block of text in a PDF viewer,
the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently.

Sample Input 1 -
- [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
- zaba
Sample Output 1
- 28
"""


def wordHeightMatcher(h):
    h = {'a': h[0], 'b': h[1], 'c': h[2], 'd': h[3], 'e': h[4], 'f': h[5], 'g': h[6], 'h': h[7], 'i': h[8], 'j': h[9],
         'k': h[10],
         'l': h[11], 'm': h[12], 'n': h[13], 'o': h[14], 'p': h[15], 'q': h[16], 'r': h[17], 's': h[18], 't': h[19],
         'u': h[20],
         'v': h[21], 'w': h[22], 'x': h[23], 'y': h[24], 'z': h[25]}
    return h


def formula(wordLen, count, maxLen):
    """
    Commented below code by for hackerrank requirements.
    :param wordLen:
    :param count:
    :param maxLen:
    :return: count
    """
    print(wordLen,count,maxLen)
    # if count > 0:
    #     return wordLen * maxLen * count
    # else:
    return wordLen * maxLen

def designerPdfViewer(h, words):
    wordLen = len(words)
    matching = wordHeightMatcher(h)
    maxLen = 0
    count = 1
    for word in words:
        if maxLen < matching.get(word):
            maxLen = matching.get(word)
        elif maxLen == matching.get(word):
            count = count + 1
        else:
            continue
    return formula(wordLen, count, maxLen)


if __name__ == '__main__':
    height = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    words = "xyz"
    calculate = designerPdfViewer(height, words)
    print(calculate)
    # print(formula(4,3,3))
