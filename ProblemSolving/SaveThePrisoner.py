"""
Function Description

Complete the saveThePrisoner function in the editor below. It should return an integer representing the chair number of the prisoner to warn.

saveThePrisoner has the following parameter(s):

    n: an integer, the number of prisoners
    m: an integer, the number of sweets
    s: an integer, the chair number to begin passing out sweets from

Sample Input 0

2
5 2 1
5 2 2

Sample Output 0

2
3
"""

def saveThePrisoner(n, m, s):
    chairs = [0] * n
    print(chairs)
    countChairs = s
    i = 0
    while i < m and countChairs < n:
        chairs[countChairs]+=1
        countChairs += 1
        i += 1
        if(countChairs >= n):
            countChairs = 0
    return chairs

if __name__ == "__main__":
    prisoners = 7
    candy = 19
    start = 2
    result = saveThePrisoner(prisoners, candy, start)
    print(result)