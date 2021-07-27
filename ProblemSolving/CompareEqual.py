A = [1,2,3,6,7,8,9]
B = [2]

def commonData(a,b):
    length = len(a) if len(a) > len(b) else len(b)
    print(length)
    
    aLen = 0
    bLen = 0
    
    answer = []
    while(aLen < length and bLen < length):
        if(a[aLen] > b[bLen]):
            bLen = bLen + 1
        elif(a[aLen] < b[bLen]):
            aLen = aLen + 1
        else:
            answer.append(a[aLen])
            aLen = aLen + 1
            bLen = bLen + 1
    print(answer)
    
commonData(A,B)    