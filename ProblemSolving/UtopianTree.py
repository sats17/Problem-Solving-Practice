"""
Function Description

Complete the utopianTree function in the editor below. It should return the integer height of the tree after the input number of growth cycles.

utopianTree has the following parameter(s):

    n: an integer, the number of growth cycles to simulate


Sample Input
3
[0,1,4]

Sample Output
[1,2,7]

"""


def getHeight(n):
    arr = [1]
    height = 1
    i = 1
    while (i <= n):
        if (i % 2 == 0):
            height += 1
            arr.append(height)
        else:
            height *= 2
            arr.append(height)
        i = i + 1
    print(arr)
    return arr


def utopianTree(n):
    answer = []
    arr = getHeight(max(n))
    for i in n:
        answer.append(arr[i])

def test(n):
    height = 1
    i = 1
    if(n == 0):
        return 0
    while (i <= n):
        if (i % 2 == 0):
            height += 1
        else:
            height = height * 2
        i = i + 1
    return height

if __name__ == '__main__':
    # a= utopianTree([0,2,1,4,15])
    # getHeight(5)
    print(0 % 2)
    a = test(0)
    print(a)