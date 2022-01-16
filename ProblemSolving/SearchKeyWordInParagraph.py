"""
Program perform word search on paragraph and return index value of paragraph where searched word is present.
"""

paragraph = "Hello my name is lucky lucky charm lucky"
word = "lucky"

"""
Algorithm: Advance naive search algorithm
Time Complexity : O(len(paragraph)) 
Need to fix
paragraph = "aaaaaaabaaab"
pattern = "aaaab" as this is not considering middle b, because we are shifting directly
"""


def getMatchedIndicesByComparingChars(paragraph, word):
    # Initialize index variable of paragraph and word
    paragraphIndex = 0
    wordIndex = 0
    matchedIndices = []  # Result storage
    while paragraphIndex <= len(paragraph) - 1:
        # run loop on each character of paragraph
        if paragraph[paragraphIndex].lower() != word[wordIndex].lower():
            # if comparison did not match between paragraph and word char, increasing paragraph iteration
            paragraphIndex += 1
            if wordIndex != 0:
                # Doing this condition and setting index for word to initialize because we want to compare the word
                # to paragraph from start
                wordIndex = 0
        else:
            # If chars matched then just moving to next iterator
            paragraphIndex += 1
            wordIndex += 1
            if wordIndex > len(word) - 1:
                # If word j index value is equal to word size then our total word is matched in paragraph
                # and we are storing index in array
                matchedIndices.append(paragraphIndex - len(word))
                wordIndex = 0
    print("matched  on index ", matchedIndices)
    return matchedIndices


def search(pat, txt):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1

        if j == M:
            print("Pattern found at index ", i)


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

"""
Work in progress

"""
def computeLPSArrayMyOwnLogic(pattern):
    patternLength = len(pattern)
    lps = [0] * patternLength
    print("Pattern length ", patternLength)
    genesis = pattern[0]
    currentMatchedIndex = -1
    isChained = False
    for i in range(1, patternLength):
        print("Current index ",pattern[i])
        if isChained:
            print("Not chained")
            # Validate currentMatchedIndex
            if pattern[currentMatchedIndex + 1] == pattern[i]:
                lps[i] = currentMatchedIndex + 1
                currentMatchedIndex = currentMatchedIndex + 1
                isChained = True

        else:
            if pattern[i] == genesis:
                currentMatchedIndex = 0
                isChained = True
                lps[i] = 1
    return lps

paragraph = "aaaaaaabaaab"
pattern = "aaaab"
M = len(pattern)
#lps = [0] * M
print(computeLPSArrayMyOwnLogic(pattern))
# print(lps)
# search(word, paragraph)
# getMatchedIndicesByComparingChars(paragraph, pattern)
