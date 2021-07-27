firstArr = [10,15,-25,2]
secondArr = [20,11,-89,-4]
blankArr = []

def diffArr(arr1,arr2,size,lastArr):
    if size == len(arr1) :
        return 0
    lastValueDiff = abs(abs(arr1[size]) - abs(arr2[size]))
    lastArr.append(lastValueDiff)
    print(lastArr)
    diffArr(arr1,arr2,size + 1,lastArr)
    return lastArr

print(diffArr(firstArr,secondArr,0,blankArr))