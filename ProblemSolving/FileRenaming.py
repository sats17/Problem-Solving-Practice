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


def combination(charArray, combinationLength, combinationValue=(), combinationList=[], test= 0):
    """
    Method generate all combinations from given array, uses recursion within each element of loop.
    Using loop we are iterating over each element and picking that element we are calling recrusive method so from
    onwards that element loop will get started to iterate.
    "What is left " We have to figure out how to return list of result from combination method
    : we can figure it out if we can use pass-by-reference to combinationList
    "What next ": Figure out how below tuple is working as by running loop our tuple should get blank
    :param test:
    :param charArray:
    :param combinationLength:
    :param combinationValue:
    :param combinationList:
    :return:
    """
    print("Start list",combinationList)
    if combinationLength == 0:
        print("combination value ",combinationValue)
        print("Added id ",id(combinationValue))
        combinationList.append(combinationValue)
        print("aftet appending value to list ",combinationList)
        return combinationList
    for x in charArray:
        print("current itertion value ",x)
        print("Before appending value ",combinationList)
        print("For loop id",id(combinationValue))
        print("Combinationvalue before ",combinationValue)
        combinationValueFormatList = list(combinationValue)
        combinationValueFormatList.append(x)  # Appending value to combination
        print("Combinaion value after append",combinationValue)
        combinationValueFormatTuple = tuple(combinationValueFormatList)
        print("After appending value ", combinationList)
        combination(charArray, combinationLength - 1, combinationValueFormatTuple, combinationList, test)
        print("Before popping list", combinationList)
        combinationPopList = list(combinationValueFormatTuple)
        combinationPopList.pop()  # Popping value from combination, after recursive combination operation done
        tuple(combinationPopList)
        print("After popping list", combinationList)
        print("value ",combinationValueFormatList)
        print("Combinationvalue after ", combinationValue)
    print("combination list ",combinationList)
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


#print(combination(['a', 'b', 'c'], 3))

tup = (1, 2, 3)
print(id(tup))
lis = list(tup)
print(id(lis))
upList = lis.append(4)
# upTuple = tuple(lis)
# upList = list(upTuple)
#upList.pop()
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
