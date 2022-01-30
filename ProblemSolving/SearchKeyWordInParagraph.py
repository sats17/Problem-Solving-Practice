"""
Program perform word search on paragraph and return index value of paragraph where searched word is present.
"""

paragraph = "Hello my name is lucky lucky charm lucky"
word = "lucky"


def patternMatchingNaiveAlgoMyOwn(paragraph, word):
    """
    Algorithm: Advance naive search algorithm
    Time Complexity : O(len(paragraph)) 
    Need to fix
    paragraph = "aaaaaaabaaab"
    pattern = "aaaab" as this is not considering middle b, because we are shifting directly
    """

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


def patternMatchingNaiveAlgo(pat, txt):
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
    timeComplexityCounter = 0
    while i < M:
        timeComplexityCounter = timeComplexityCounter + 1
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
    print("Time Complexity ", timeComplexityCounter)


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

    genesis = pattern[0]
    currentIndex = 0  # Current matching index of pattern
    isChained = False  # Flag to check if pattern is chained or not

    for i in range(1, patternLength):
        if isChained:
            # Validate currentIndex with current character of loop
            if pattern[currentIndex] == pattern[i]:
                lps[i] = currentIndex + 1
                currentIndex = currentIndex + 1
                isChained = True
            # Validation for previous index of chain with current character of loop and previous index of of loop
            # with previous to previous currentIndex. This condition is here to satiesfy the if chain
            # is having same characters or not
            elif pattern[i] == pattern[currentIndex - 1] and pattern[i - 1] == pattern[currentIndex - 2]:
                lps[i] = currentIndex
                isChained = True
            # if above valiation failed, then we will validate with genesis block
            elif genesis == pattern[i]:
                lps[i] = 1
                currentIndex = 0
                isChained = True
            # If nothing is matched then we will break chain
            else:
                lps[i] = 0
                currentIndex = 0
                isChained = False
        else:
            if pattern[currentIndex] == pattern[i]:
                lps[i] = currentIndex + 1
                isChained = True
                currentIndex = currentIndex + 1
            else:
                lps[i] = 0
    return lps

def patternMatchingKMP(txt, pat):
    """
    Build own different logic for KMP algo by refereing psuedo code from geeksforgeeks.
    Found out why there is elif condition in KMP algo.
    """
    patLen = len(pat)
    txtLen = len(txt)
    lps = computeLPSArrayMyOwnLogic(pat)
    print("LPS is = ", lps)
    patIndex = 0
    txtIndex = 0
    counter = 0
    while txtIndex < txtLen:
        print("txtIndex = ", txtIndex," txtValue = ", txt[txtIndex], " patIndex = ", patIndex, " patValue = ", pat[patIndex])
        counter = counter + 1
        if pat[patIndex] == txt[txtIndex]:
                patIndex += 1
                txtIndex += 1
        if patIndex == patLen:
                print("Pattern found at index ", txtIndex - patLen)
                patIndex = lps[patIndex - 1]
        else:
            if patIndex < 1:
                print("last if")
                txtIndex += 1
            else:
                print("last else")
                patIndex = lps[patIndex - 1]
    print("Counter ", counter)

# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    count = 0
	# create lps[] that will hold the longest prefix suffix
	# values for pattern
    lps = [0]*M
    j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
    lps = computeLPSArrayMyOwnLogic(pat)

    i = 0 # index for txt[]
    while i < N:
        count = count + 1
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]

		# mismatch after j matches
        elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
            if j != 0:
                j = lps[j-1]    
            else:
                i += 1
    print(count)


txt = "baaabaaaaabaaa"
pat = "aaab"
KMPSearch(pat, txt)
print("started my kmp")
patternMatchingKMP(txt, pat)
# M = len(pattern)
# print(pattern)
# lps2 = [0] * M

# print(computeLPSArrayMyOwnLogic(pattern))
# computeLPSArray(pattern, M, lps2)
# print(list(pattern))
# print(lps2)
# print(lps)
# search(word, paragraph)
# getMatchedIndicesByComparingChars(paragraph, pattern)
# https://towardsdatascience.com/pattern-search-with-the-knuth-morris-pratt-kmp-algorithm-8562407dba5b
