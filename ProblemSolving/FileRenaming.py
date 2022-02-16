"""
You have to find ways that after how many times character deletes from old file name we can get newFileName.
Both oldFileName and newFileName is given.
example :

for renameFile2 method
input = old - aaabbbccc
        new - abc
output - 27

for renameFile method
input = old - aaabbbccc
        new - abc
output - 0 (because only consecutive character deletion allowed)

"""
from itertools import combinations


def renameFile(newName, oldName):
    """
    This will give answers for only consecutive characters are allowed to delete.
    Like if we have newFileName abc, and old is abcba then only (abc)ba can get delete here because it is consecutive.
    """
    diffNum = len(oldName) - len(newName)
    count = 0
    for i in range(0, len(oldName)):
        modifiedOldName = ""
        for j in range(len(oldName)):
            arr = []
            for num in range(diffNum):
                arr.append(i + num)
            if j not in arr:
                modifiedOldName = modifiedOldName + oldName[j]
        if newName == modifiedOldName:
            count = count + 1
    return count


def renameFileUsingOurOwnCombinationLogic(newName, oldName):
    """
    :param newName:
    :param oldName:
    :return:
    """
    oldNameCharsList = []
    newNameCharsList = []
    newNameMatchingCounter = 0
    for i in oldName:
        oldNameCharsList.append(i)
    for i in newName:
        newNameCharsList.append(i)
    combinationsListForOldName = combination(oldNameCharsList, len(newName))
    for i in combinationsListForOldName:
        if newNameCharsList == list(i):
            newNameMatchingCounter = newNameMatchingCounter + 1
    return newNameMatchingCounter
    # Working on how we can found out all possible ways to iterate oldName(Or any array)
    # Last seen was https://www.geeksforgeeks.org/iterating-over-all-possible-combinations-in-an-array-using-bits/


def renameFileUsingItertoolsCombination(newName, oldName):
    oldNameCharsList = []
    newNameCharsList = []
    newNameMatchingCounter = 0
    for i in oldName:
        oldNameCharsList.append(i)
    for i in newName:
        newNameCharsList.append(i)
    combinationsListForOldName = list(combinations(oldNameCharsList, len(newName)))
    for i in combinationsListForOldName:
        if newNameCharsList == list(i):
            newNameMatchingCounter = newNameMatchingCounter + 1
    return newNameMatchingCounter


def combination(charArray, combinationLength, combinationValue=(), combinationList=[], offset=0):
    """
    Method generate all combinations of elements from given array, it uses recursion inside iteration of array elements.
    So for every i th element we are calling recursive method which has decreasing length and combination appended value.
    At last when size reduced to 0 we are returning appended combination value. and next iteration will run as it is.

    This method does not pick duplicate elements like for a,b,c,d,e data with length 3 it will not consider a,a,a hence
    we used offset which tells loop to start with next element from previous loop.

    Also we need to return collected combination so we are using list and tuple here. as we cannot pass list in recursion
    method because pass by reference update issue, we are passing tuple here so it can have it's individual values.

    Note : for python we don't require popping after recursive method
    :param charArray: characters array from that we want combination
    :param combinationLength: what length of combination we want
    :param combinationValue: Single combination value
    :param combinationList: List of combinations
    :param offset: offset use to do not iterate loop from start as we want our combination unique.
    :return:
    """
    if combinationLength == 0:
        combinationList.append(combinationValue)
        return combinationList
    for index in range(offset, len(charArray)):
        combinationValueFormatList = list(combinationValue)
        combinationValueFormatList.append(charArray[index])  # Appending value to combination
        # which is helping us not to remove elements from final list when we popped.
        combination(charArray, combinationLength - 1, tuple(combinationValueFormatList), combinationList, index + 1)
        # combinationPopList = list(combinationValueFormatList)
        # print("After recursion ", combinationValueFormatList)
        # Commenting pop here as we are not required
        # combinationValueFormatList.pop()  # Popping value from combination, after recursive combination operation done
        # tuple(combinationValueFormatList.pop())
    return combinationList


def dynamicLoop(arr, length):
    """
    Method run dynamic loop using recursion, by decreasing length for each field of loop we
    are iterating.
    :param arr:
    :param length:
    :param lis:
    :return:
    """
    if length == 0:
        return
    for i in arr:
        print("Calling other loop from ", i)
        dynamicLoop(arr, length - 1)


print(combination(['a', 'b', 'c','d'], 3))

#print("Total combination we can get ", renameFileUsingOurOwnCombinationLogic("abc", "aaabbbccc"))


