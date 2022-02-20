def isUgly(num):
    if num <= 0:
        return False
    while num % 2 == 0:
        print("num is ",num)
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5
    print("num is ",num)
    return num == 1
# print(isUgly(1878))
answer = []
for i in range(1,50):
    if isUgly(i): 
        answer.append(i)
print(answer.__len__())
print(answer[19])