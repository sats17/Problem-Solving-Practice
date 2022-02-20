"""
Function Description

Complete the pairs function below. It must return an integer representing the number of element pairs 
having the required difference.

pairs has the following parameter(s):

    k: an integer, the target difference
    arr: an array of integers

Sample Input
2
1 5 3 4 2
Sample Output
3
"""

def pairs(k, arr):
    count = 0
    arrLen = len(arr)
    for i in range(0,arrLen - 1):
        for j in range(i+1,arrLen):
            l = [1, 3, 2, 5, 4]
            # 1 + 2 = 3
            if(abs(arr[i] - arr[j]) == k):
                # 1 - 2 = 2
                count +=1
                break
    return count

def pairsAdvance(k, arr):
    arr.sort()
    print("After sorted array is ",arr)
    arrLen = len(arr)
    nextIndex = 1
    currentIndex = 0
    count = 0
    while nextIndex < arrLen:
        diff = arr[nextIndex] - arr[currentIndex]

        if diff == k:
            count +=1
            nextIndex +=1
            currentIndex += 1
        elif diff > k:
            currentIndex +=1
        else:
            nextIndex += 1
    return count

def memoizedPairsDiff(k, arr):
    """
    In memoization logic, we are just putting the array values into hashset(o(1) Complexity))),
    by doing this we are just doing sum of current iteration and k, if this value present in hashset. 
    Then it contains the pair.
    Unfortunately we required reverse sort if we want to find the pair of diff k. We do reverse sorting here
    because there won't be any number greater than first number in reverse sorted array.
    # To sum up, we are doing O(n) complexity. And we required reverse sorted array plus hashset to find the pairs.
    arr = [9, 5, 3, 4, 2, 11]
    """
    print("Incoming array ",arr)
    print("Required diff is ",k)
    arr.sort(reverse=True) # sort in descending order, required if you are finding the pairs with diff k
    memoizedArr = set()
    count = 0
    for i in arr:
        print("i is ",i)
        sum = i + k
        if(sum in memoizedArr):
            print("Found a pair ",i,"+",k,"=",sum)
            count +=1
            memoizedArr.add(i)
        else:
            memoizedArr.add(i)
    print("Diff is ",k)
    print("Array is ",arr)
    print("Memoized array is ",memoizedArr)
    return count

def memoizedFindPairAdvanced(k, arr):
    """
    This version we tried to make it advanced. In this version we are converting the array into hashset.
    Then we are finding if the sum present in hashset or not.
    """
    print("Array ",arr)
    hashSet = set()
    count = 0
    for i in arr:
        hashSet.add(i)
    print("Hashset is ",hashSet)
    for i in arr:
        sum = i + k
        if(sum in hashSet):
            print("Found a pair ",i,"+",k,"=",sum)
            count +=1
    return count

if __name__ == "__main__":
    arr = [9, 5, 3, 4, 2, 7, 11]
    # result = pairsAdvance(2,arr)
    # # print("Result is ",pairs(2,arr))
    # print("pair advance result ",result)
    # print(memoizedPairsDiff(2,arr))
    print(memoizedFindPairAdvanced(2,arr))
    # driver code
    # A = [9, 5, 3, 4, 2, 11]
    # n = 2
    # printPairs(A, len(A), n)