"""
Function Description

Complete the viralAdvertising function in the editor below. It should return the cumulative number of people who have
liked the ad at a given time.

viralAdvertising has the following parameter(s):

    n: the integer number of days

Sample Input

3

Sample Output

9

"""

def viralAdvertising(n):
    likes = 0
    people = 5
    for i in range(1,n+1):
        likes = likes + (people // 2)
        people = (people // 2) * 3
    return likes

if __name__ == "__main__":
    days = 0
    output = viralAdvertising(days)
    print(output)