"""
Program perform word search on paragraph and return index value of paragraph where searched word is present.
"""

paragraph = "Hello my name is lucky lucky charm lucky"
word = "lucky"

"""
Time Complexity : O(len(paragraph)) 
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


# search(word, paragraph)
getMatchedIndicesByComparingChars(paragraph, word)
