num = 3

sum1 = 0
flag = 1
for i in range(num,500000,3):
    if(i % 5 == 0):   
        continue
    sum1 = sum1 + i
    flag = flag + 1

for i in range(5,500000,5):
    sum1 = sum1 + i
    flag = flag + 1
    
# print(sum1)
# flag = 1
# for i in range(1,500000):
#     flag = flag + 1
#     if(i % 5 == 0 or i % 3 == 0):
#         sum1 = sum1 + i

print(sum1)
print(flag)