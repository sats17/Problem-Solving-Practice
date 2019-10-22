first = 1
second = 1
third = 2

for i in range(first,8):
    for j in range(second,8):
        if(i + j > 10 or i == j):
            continue
        for k in range(third,7,2):
            if(i + j + k != 12 or i == k or j == k or i + k > 10 or j + k > 10):
               continue
            print("f ",i ,"s  ", j , "t ", k)