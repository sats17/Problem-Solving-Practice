"""
Program perform word search on paragraph and return index value of paragraph where searched word is present.
"""

paragraph = "Sunset is the time of day when our sky meets the outer space solar winds. " \
            "There are blue, pink, and purple swirls, spinning and twisting, like clouds of " \
            "balloons caught in a whirlwind. The sun moves slowly to hide behind the line of horizon, " \
            "while the moon races to take its place in prominence atop the night sky. People slow to a crawl," \
            " entranced, fully forgetting the deeds that must still be done. There is a coolness, a calmness, " \
            "when the sun does set."
word = "the"

"""
Time Complexity : O(len(paragraph)) 
"""
def getMatchedIndicesByComparingChars(paragraph, word):
    # Initialize index variable of paragraph and word
    i = 0
    j = 0
    matchedIndices = []  # Result storage
    while i <= len(paragraph) - 1:
        # run loop on each character of paragraph
        if paragraph[i].lower() != word[j].lower():
            # if comparison did not match between paragraph and word char, increasing paragraph iteration
            i += 1
            if j != 0:
                # Doing this condition and setting index for word to initialize because we want to compare the word
                # to paragraph from start
                j = 0
        else:
            # If chars matched then just moving to next iterator
            i += 1
            j += 1
            if j > len(word) - 1:
                # If word j index value is equal to word size then our total word is matched in paragraph
                # and we are storing index in array
                matchedIndices.append(i - len(word))
                j = 0
    print("matched  on index ", matchedIndices)
    return matchedIndices


getMatchedIndicesByComparingChars(paragraph, word)
