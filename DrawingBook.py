"""
Function Description

Complete the pageCount function in the editor below. It should return the minimum number of pages Brie must turn.

pageCount has the following parameter(s):

    n: the number of pages in the book
    p: the page number to turn to


Sample Input 1

5
4

Sample Output 1

0
"""

def pageCount(n, p):
    mid = n // 2
    count = 0
    if p <= mid:
        print(p // 2)
        count = p // 2
    else:
        reveseIndex = n
        while p < reveseIndex:
            if reveseIndex % 2 == 0:
                print("gets here")
                count += 1
            reveseIndex -= 1
    return count

if __name__ == "__main__":
    result = pageCount(10,6)
    print(result)
    arr = [0,1,2,3,4,5,6,7,8,9,10]