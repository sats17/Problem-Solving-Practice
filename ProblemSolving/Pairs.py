"""
Function Description

Complete the pairs function below. It must return an integer representing the number of element pairs having the required difference.

pairs has the following parameter(s):

    k: an integer, the target difference
    arr: an array of integers

Sample Input

5 2
1 5 3 4 2

Sample Output

3


"""

def pairs(k, arr):
    count = 0
    arrLen = len(arr)
    for i in range(0,arrLen - 1):
        for j in range(i+1,arrLen):
            if(abs(arr[i] - arr[j]) == k):
                count +=1
                break
    return count

def pairsAdvance(k, arr):
    arr.sort()
    arrLen = len(arr)
    nextIndex = 1
    currentIndex = 0
    count = 0
    while nextIndex < arrLen:
        print("i")
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

if __name__ == "__main__":
    arr = [4, 7, 8, 9, 11]
    result = pairsAdvance(2,arr)
    print(result)
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