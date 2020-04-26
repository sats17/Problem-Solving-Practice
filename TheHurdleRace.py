"""
Function description -

Complete the hurdleRace function in the editor below. It should return the minimum units of potion Dan needs to drink to jump all of the hurdles.

hurdleRace has the following parameter(s):

    k: an integer denoting the height Dan can jump naturally
    height: an array of integers denoting the heights of each hurdle


Sample Input-
5 4
1 6 3 5 2

Sample Output
2

"""

def hurdleRace(k, height):
    maxHeight = max(height)
    difference = maxHeight - k
    if(difference <= 0):
        return 0
    else:
        return difference


if __name__ == '__main__':
    doses = hurdleRace(1,[4,3,4,5,5,5])
    print(doses)