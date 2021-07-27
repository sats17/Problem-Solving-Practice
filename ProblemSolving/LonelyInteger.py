arr = [1,1,2]

def findLonelyMyLogic(arr):
    arr.sort()
    lenArr = len(arr) - 1
    i = 0
    while(i <= lenArr):
        current = arr[i]
        count = 0
        i+=1
        while(i <= lenArr and current == arr[i]):
            count+=1
            i+=1
        if(count == 0):
            return arr[i - 1]
            break

def findLonelyUsingXOR(arr):

    return 5
print(2 ** 2)
print(findLonelyMyLogic(arr))