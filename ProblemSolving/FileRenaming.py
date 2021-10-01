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
    diffNum = len(oldName) - len(newName)
    count = 0
    oldNameCounter = 0
    newNameCounter = 0
    while oldNameCounter < len(oldName):
        insideOldNameCounter = oldNameCounter
        insideNewNameCounter = newNameCounter
        if oldName[oldNameCounter] == newName[newNameCounter]:
            insideOldNameCounter
        oldNameCounter = oldNameCounter + 1
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


def renameFileUsingCombination(newName, oldName):
    return


combinationResult = []


def combination(charArray, combinationLength, combinationValue=(), combinationList=[]):
    """
    Method generate all combinations of elements from given array, it uses recursion inside iteration of array elements.
    So for every i th element we are calling recursive method which has decreasing size and combination appended value.
    At last when size reduced to 0 we are returning appended combination value. and next iteration will run as it is.

    Also we need to return collected combination so we are using list and tuple here. as we cannot pass list in recursion
    method because pass by reference update issue, we are passing tuple here so it can have it's individual values.

    Note : for python we don't require popping afte recursive method
    :param test:
    :param charArray:
    :param combinationLength:
    :param combinationValue:
    :param combinationList:
    :return:
    """
    if combinationLength == 0:
        combinationList.append(combinationValue)
        return combinationList
    for x in charArray:
        print(combinationValue)
        combinationValueFormatList = list(combinationValue)
        combinationValueFormatList.append(x)  # Appending value to combination
        # which is helping us not to remove elements from final list when we popped.
        combination(charArray, combinationLength - 1, tuple(combinationValueFormatList), combinationList)
        # combinationPopList = list(combinationValueFormatList)
        # print("After recursion ", combinationValueFormatList)
        # Commenting pop here as we are not required
        # combinationValueFormatList.pop()  # Popping value from combination, after recursive combination operation done
        # tuple(combinationValueFormatList.pop())
    print("combination list ", combinationList)
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


print(combination(['a', 'b', 'c'], 2))

tup = (1, 2, 3)
print(id(tup))
lis = list(tup)
print(id(lis))
upList = lis.append(4)
# upTuple = tuple(lis)
# upList = list(upTuple)
# upList.pop()
tuple(lis)
print(tup)
# print(id(li))
# print(li)
# def testPas(li):
#     li.append(4)
#     print(id(li))
# testPas(li)
# print(li)
# print(combinationResult)
# print("Total combination we can get ", renameFileUsingItertoolsCombination("d", "aaabbbccc"))
