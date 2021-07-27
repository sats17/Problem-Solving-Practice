s1 = "abcdef"
s2 = "abcd"

def convt(str):
    return [char for char in str]

def isOneAway(s1,s2):
    s1Arr = convt(s1)
    s2Arr = convt(s2)
    diff = abs(len(s1Arr) - len(s2Arr))
    if(diff > 1):
        return False
    s1Arr = sorted(s1Arr)
    s2Arr = sorted(s2Arr)
    i = 0
    j = 0
    count = 0
    while(i < len(s1Arr) and j < len(s2Arr)):
        if(ord(s1Arr[i]) < ord(s2Arr[j])):
            i+=1
            count +=1
        elif(ord(s1Arr[i]) < ord(s2Arr[j])):
            j+=1
            count+=1
        else:
            i+=1
            j+=1
        if(count > 1):
            return False

    return True

print(isOneAway(s1,s2))
