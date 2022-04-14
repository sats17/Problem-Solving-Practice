def getSumCombination(number, array):
    if number == 0:
        return 1
    if number < 0:
        return 0
    if len(array) == 0:
        return 0
    return getSumCombination(number, array[1:]) + getSumCombination(number - array[0], array)

print(getSumCombination(10, [1, 2, 3, 4, 5]))

    