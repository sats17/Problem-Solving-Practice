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
    Unfortunately we required reverse sort if we want to find the pair of diff k.
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

if __name__ == "__main__":
    arr = [9, 5, 3, 4, 2, 7, 11]
    result = pairsAdvance(2,arr)
    # print("Result is ",pairs(2,arr))
    print("pair advance result ",result)
    print(memoizedPairsDiff(2,arr))
    # driver code
    # A = [9, 5, 3, 4, 2, 11]
    # n = 2
    # printPairs(A, len(A), n)
"""
    var
    i = 0, j = 1, count = 0;

    while (j < n) {
    var diff = nums[j] - nums[i];

    if (diff == k) {
    count++;
    j++;
    } else if (diff > k) {
    i++;
    } else if (diff < k) {
    j++;
    }
    }"""