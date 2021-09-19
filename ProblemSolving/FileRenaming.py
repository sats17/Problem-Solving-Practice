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


def renameFile2(newName, oldName):
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


print(renameFile2("abc", "abcbc"))
