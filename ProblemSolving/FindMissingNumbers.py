"""
Logic - Iterate over the array, get difference between currentIndex and nextIndex. if difference is not
equal to zero then iterate currentIndex + 1 till less than next index and append all values in missing array.s
"""

def findMissingNumbers(arr, start, end):
    missingValues = []
    for i in range(0, len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if diff != 0:
            missing = arr[i] + 1
            while missing < arr[i+1]:
                missingValues.append(missing)
                missing += 1
    return missingValues

arr = [1, 2, 4, 6, 7, 12, 20]
start = 1
end = 20
print(findMissingNumbers(arr, start, end))