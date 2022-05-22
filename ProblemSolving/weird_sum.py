"""
Some quetions that I got in interview
"""

def weirdSum(N, arr):
    sum = 0
    for i in arr:
        if i == N:
            continue
        sum = sum + i
    return sum


def maxiPow(arr, K):
    totalOdd = 0
    maxHeight = 0
    totalThrows = 0
    for i in range(0, len(arr)):
        if i == 0:
            if arr[i] % 2 != 0:
                totalOdd = totalOdd + 1
            totalThrows = totalThrows + 1
            maxHeight = arr[i]
            continue
        if arr[i] <= maxHeight:
            continue
        else:
            maxHeight = arr[i]
            totalThrows = totalThrows + 1
        if arr[i] % 2 != 0:
            totalOdd =+ 1
    return totalThrows



arr = [1, 6, 7, 1, 2]
print(maxiPow(arr, 4))
