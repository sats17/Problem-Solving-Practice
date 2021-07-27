arr = [[1,2,3],[4,5,6],[7,8,9]]

def setIndex(i,j,n):
    return j,n - 1 - i

def rotate(arr):
    a = setIndex(2,4,5)
    length = len(arr)
    duplicateArr = [[0 for col in range(3)] for row in range(3)]
    for i in range(length):
        for j in range(length):
            newIndex = setIndex(i,j,length)
            duplicateArr[newIndex[0]][newIndex[1]] = arr[i][j]
    print(duplicateArr)


rotate(arr)