"""
Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys
Gary traversed.

countingValleys has the following parameter(s):
n: the number of steps Gary takes
path: a string describing his path


Sample Input
8
UDDDUDUU

Sample Output
1

"""

def countingValleys(n,path):
    print(n)
    print(path)
    seaLevel = 0
    valley = 0
    isDown = False
    for direction in path:
        if direction == 'U':
            seaLevel = seaLevel + 1
        elif direction == 'D':
            seaLevel = seaLevel - 1
            if(seaLevel < 0):
                isDown = True
            else:
                isDown = False
        else:
            continue
        print(direction)
        if (isDown and seaLevel == 0):
            print("isDown")
            valley = valley + 1
    print(valley)
    print(seaLevel)


if __name__ == '__main__':
    countingValleys(8,'UDDDUDUU')