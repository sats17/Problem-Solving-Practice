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
    loopConter = 0
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
            loopConter = loopConter + 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]
                loopConter = loopConter + 1
            else:
                lps[i] = 0
                i += 1
                loopConter = loopConter + 1
    print("Loop counter ", loopConter)

"""
Work in progress

"""
def computeLPSArrayMyOwnLogic(pattern):
    """
    This logic takes pattern and add value of each index of character in pattern, which added value
    tells that that much length of prefix in pattern is matched with suffix of pattern till that index.
    :param pattern:
    :return:
    """
    patternLength = len(pattern)
    lps = [0] * patternLength
    lps[0] = 0
    print("Pattern length ", patternLength)

    genesis = pattern[0]
    currentIndex = 0 # Current matching index of pattern
    isChained = False # Flag to check if pattern is chained or not

    loopCounter = 0
    for i in range(1, patternLength):
        if isChained:
            # Validate currentIndex with current character of loop
            if pattern[currentIndex] == pattern[i]:
                lps[i] = currentIndex + 1
                currentIndex = currentIndex + 1
                isChained = True
                loopCounter = loopCounter + 1
            # Validation for previous index of chain with current character of loop and previous index of of loop
            # with previous to previous currentIndex. This condition is here to satiesfy the if chain 
            # is having same characters or not
            elif pattern[i] == pattern[currentIndex - 1] and pattern[i - 1] == pattern[currentIndex - 2]:
                lps[i] = currentIndex
                isChained = True
                loopCounter = loopCounter + 1
            # if above valiation failed, then we will validate with genesis block
            elif genesis == pattern[i]:
                lps[i] = 1
                currentIndex = 0
                isChained = True
                loopCounter = loopCounter + 1
            # If nothing is matched then we will break chain
            else:
                lps[i] = 0
                currentIndex = 0
                isChained = False
                loopCounter = loopCounter + 1
        else:
            if pattern[currentIndex] == pattern[i]:
                lps[i] = currentIndex + 1
                isChained = True
                currentIndex = currentIndex + 1
                loopCounter = loopCounter + 1
            else:
                lps[i] = 0
                loopCounter = loopCounter + 1
    print("Loop counter from my ", loopCounter)
    return lps

paragraph = "aaaaaaabaaab"
pattern = "aaaaaaabaaab" # Need to check on this pattern
M = len(pattern)
print(pattern)
lps2 = [0] * M

print(computeLPSArrayMyOwnLogic(pattern))
computeLPSArray(pattern, M, lps2)
print(list(pattern))
print(lps2)
# print(lps)
# search(word, paragraph)
# getMatchedIndicesByComparingChars(paragraph, pattern)
# https://towardsdatascience.com/pattern-search-with-the-knuth-morris-pratt-kmp-algorithm-8562407dba5b
