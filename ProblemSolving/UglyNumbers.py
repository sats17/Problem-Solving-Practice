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
for i in range(1,10):
    if isUgly(i): 
        answer.append(i)
print(answer)
# print(answer.__len__())
# print(answer[19])
"""
Next action item:
Following this https://medium.com/@interviewprep/ugly-number-dynamic-programming-94520110a084
Working on logic of heap and min heap data structure.
In above logic they are multiplying by 2,3,5 starting from 1. And when we have data of multiplication
then by picking the minimum value of multiplication we can get the next values. also our minimum values
are ugly numbers
"""