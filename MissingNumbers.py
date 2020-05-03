"""
Function Description

Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.

missingNumbers has the following parameter(s):

    arr: the array with missing numbers
    brr: the original array of numbers

Sample Input

10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204

Sample Output

204 205 206

"""


def missingNumbers(arr, brr):
    result = []
    arrLen = len(arr)
    arr.sort()
    brrLen = len(brr)
    brr.sort()
    arrIndex = 0
    brrIndex = 0
    print(arr)
    print(brr)
    while(arrIndex < arrLen and brrIndex < brrLen):
        if(arr[arrIndex] == brr[brrIndex]):
            brrIndex += 1
            arrIndex += 1
        else:
            print(brr[brrIndex])
            if brr[brrIndex] not in result:
                result.append(brr[brrIndex])
            brrIndex += 1
    print(brrIndex)
    while(brrIndex < brrLen):
        if brr[brrIndex] not in result:
            result.append(brr[brrIndex])
        brrIndex+=1
    result.sort()
    return result


if __name__ == "__main__":
    arr = [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
    brr = [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]
    result = missingNumbers(arr,brr)
    print(result)
