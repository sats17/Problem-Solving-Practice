buildings = [2,3,4,5,9]
def towerFit(buildings,transRange):
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
        print("Tower yahi banega", buildings[i])
        print(i)
        transMitterRange = buildings[i] + transRange
        print(transMitterRange)

       # transMitterRange = buildings[i] + transRange
        while(i < len(buildings) - 1 and buildings[i] <= transMitterRange ):
            print("second",i)
            i+=1
        print("outer",i)
towerFit(buildings,0)