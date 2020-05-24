import pdb
"""
Function Description

Complete the hackerlandRadioTransmitters function in the editor below. It must return an integer that denotes the minimum number of transmitters to install.

hackerlandRadioTransmitters has the following parameter(s):

    x: integer array that denotes the locations of houses
    k: an integer that denotes the effective range of a transmitter


Sample Input 0

5 1
1 2 3 4 5

Sample Output 0

2

"""

def hackerlandRadioTransmittersDecre(buildings,transRange):
    i = 0
    length = len(buildings) - 1
    print(length)
    while(i < length):
        print("main",i)
        transMitterRange = buildings[i] + transRange
        while(i < length  and buildings[i] <= transMitterRange):
            print("first",i)
            i = i + 1

        i-=1
        print(i)
        transMitterRange = buildings[i] + transRange
        print(transMitterRange)

       # transMitterRange = buildings[i] + transRange
        while(i < len(buildings) - 1 and buildings[i] <= transMitterRange ):
            print("second",i)
            i+=1
        print("outer",i)

def hackerlandRadioTransmitters(x,k):
    x.sort();
    if(len(x) == 1):
        return 1
    xLen = len(x) - 1
    i = 0
    towers = []
    flag = False
    count = 0
    while i < xLen:
        count += 1
        transmitterRange = x[i] + k
        while i < xLen and x[i] <= transmitterRange:
            print(transmitterRange)
            i += 1
            flag = True
        if(flag):
            i -= 1
            flag = False
        towerPlace = x[i]
        towers.append(towerPlace)
        transmitterRange = x[i] + k
        while i < xLen and x[i] <= transmitterRange:
            i += 1
    if(x[i] - towers[-1] > k):
        count += 1
        towers.append(x[i])
    return count

if __name__ == "__main__":
    #[2, 4, 5, 6, 7, 9, 11, 12]
    buildings = [7, 2, 4, 6, 5, 9, 12, 11]
    buid = [1]
    # transmitterRange = 2
    result = hackerlandRadioTransmitters(buid,1)
    print(result)