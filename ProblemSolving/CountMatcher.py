"""
Function Description

Function prints total number of pairs whose sum is k, print 0 if no pair founds.

calculate function has the following parameter(s):
nList: list of the numbers
k: sum value


Sample Input
nList - [5,1,2,3,4]
k - 6
Sample Output
2
"""
import datetime
import time


def search(lst, target):
    min = 0
    max = len(lst) - 1
    avg = (min + max) // 2
    # uncomment next line for traces
    # print lst, target, avg
    while (min < max):
        if (lst[avg] == target):
            return avg
        elif (lst[avg] < target):
            return avg + 1 + search(lst[avg + 1:], target)
        else:
            return search(lst[:avg], target)

    # avg may be a partial offset so no need to print it here
    # print "The location of the number in the array is", avg
    return avg


def calculateBruteForce(nList, k):
    result = 0
    for i in range(0, len(nList)):
        rootElement = nList[i]
        for j in range(i + 1, len(nList)):
            childElement = nList[j]
            if rootElement + childElement == k:
                result = result + 1
    print(result)


def calculateUsingBinarySearch(nList, k):
    result = 0

    nList.sort()
    middleElement = 17 // 2
    print(middleElement)
    index = nList[search(nList, middleElement)]
    print(index)
    print()
    # while middleElement <= k:
    #     i = 0
    #     while i <= len(nList) and i
    #         if i + nList[index] == k:
    #             result = result + 1


# [0,1,2,3,4,5,6,7,10]


nList = [0, 1, 2, 3, 4, 5, 6, 7, 10]
k = 6

#calculateUsingBinarySearch(nList, k)
exe = 0
for i in range(0, 10):
    start_time = datetime.datetime.now()
    calculateBruteForce(nList, k)
    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    exe = exe + execution_time
print(exe)
