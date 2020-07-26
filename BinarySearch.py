"""
Binary Search
Flow -
var = rightIndex = arrLen - 1
1) Get middle index of array [ leftIndex + ((rightIndex - startIndex) // 2))]
2) Compare searchValue with middle index value
3) If it equal return with index[Index shows here is your searchValue present]
4) If it searchValue is greater, then change leftIndex is equal to middle index  + 1, and repeat step 1
5) If searchValue is lesser, then change rightIndex is equal to middle index - 1, and repeat step 1
6) If rightIndex is greaterThan equal to leftIndex then return value not found.

"""

def binarySearch(arr, leftIndex, rightIndex, value):

    if rightIndex >= leftIndex:
        mid = leftIndex + (rightIndex - leftIndex) // 2
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            return binarySearch(arr, mid + 1, rightIndex, value)
        else:
            return binarySearch(arr, leftIndex, mid - 1, value)
    else:
        return -1


arr = [1,2,3,4,5,11,25,67,98]
print("answer is ",arr[binarySearch(arr, 0, len(arr) - 1, 67)])