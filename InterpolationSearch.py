import time
"""
INTERPOLATION SEARCH
Variables -
lowIndex = 0th position of array index
highIndex = nth position of array index
x = element to be search in array
arr = Searchable sorted array with uniformly distributed values
arr[lowIndex] = 0th index element of array
arr[highIndex] = nth index element of array

PositionFormula =
lowIndex + (( x - arr[lowIndex] ) / (arr[highIndex] - arr[lowIndex]) ) * ( highIndex - lowIndex )

FunctionDescription =
Function Takes 2 parameter, arr = Array which it has all data and x = element that is going to searched.

Flow =
1) Basic check with high index and low index, if matches then return with element found.
2) If lowIndex is less than equal to highIndex and x less than or equal to arr[highIndex] and x is greater
than equal to arr[lowIndex] then enter in loop or return with no element found.
3) Calculate interpolation formula and if arr[pos] is equal to x then return element found.
4) if arr[pos] is greater than x then make highIndex = arr[pos] - 1. If arr[pos] is less than x then make
lowIndex = arr[pos] + 1. and repeat step 2.

"""

def InterPolationSearch(arr, x):
    lowIndex = 0
    highIndex = len(arr) - 1
    # Basic checks
    if x == arr[lowIndex]:
        return "Element Found at index, ", lowIndex
    if x == arr[highIndex]:
        return "Element Found at index, ", highIndex
    while lowIndex <= highIndex and x <= arr[highIndex] and x >= arr[lowIndex]:
        # Interpolation Formula
        pos = lowIndex + (( x - arr[lowIndex] ) / (arr[highIndex] - arr[lowIndex]) ) * ( highIndex - lowIndex )
        convtPos = int(pos)
        if arr[convtPos] == x:
            return "Element Found at index, ",convtPos
        elif arr[convtPos] < x:
            lowIndex = convtPos + 1
        else:
            highIndex = convtPos - 1
    return "Element Not found"



arr = []
for i in range(0,100000000,4):
    arr.append(i)
x = 9999123127032
print(arr)
Enter = time.time()
print(InterPolationSearch(arr, x))
End = time.time()
print("Total time search takes ", End - Enter)


#  / 18 * 9
