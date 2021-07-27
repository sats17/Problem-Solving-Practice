"""
Function Description

Complete the getMoneySpent function in the editor below. It should return the maximum total price for the two items within Monica's budget, or

if she cannot afford both items.

getMoneySpent has the following parameter(s):

    keyboards: an array of integers representing keyboard prices
    drives: an array of integers representing drive prices
    b: the units of currency in Monica's budget

Sample Input 0

10 2 3
3 1
5 2 8

Sample Output 0

9
"""

def getMoneySpent(keyboards, drivers, b):
    keyboards.sort(reverse = True)
    drivers.sort(reverse = True)
    cost = -1
    for i in keyboards:
        for j in drivers:
            if i + j <= b and i + j > cost:
                cost = i + j

    return cost

if __name__ == "__main__":
    keyboards = [3, 1]
    drivers = [5, 2, 8]
    result = getMoneySpent(keyboards, drivers, 1)
    print(result)