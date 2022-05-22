from itertools import permutations
from operator import contains

def combination(charArray, combinationLength, combinationValue=(), combinationList=[], offset=0):
    """
    Method generate all combinations of elements from given array, it uses recursion inside iteration of array elements.
    
    So for every i th element we are calling recursive method which has parameter of decreasing length of combination and storing that i th element as a 
    combination appended result value.
    At last when size reduced to 0 we are returning appended combination value. Then we are doing return statement, which routes to
    last most recursive method and iteration present in that recursive method will either go to next element or return. This will be 
    there for each recursive call.

    This method does not pick duplicate elements like for a,b,c,d,e data with length 3 it will not consider a,a,a hence
    we used offset which tells loop to start with next element from previous loop.

    Also we need to return collected combination so we are using list and tuple here. as we cannot pass list in recursion
    method because pass by reference update issue, we are passing tuple here so it can have it's individual values.
    Example: a, b, c, d : combinationLength = 3
    1st iteration: a, b, c
    2nd iteration: a, b, d
    3rd iteration: a, c, d
    4th iteration: b, c, d
    
    When there is no more elements to iterate, we are returning combinationList. Example: 
    for above example, after 3rd iteration for C element loop will go to next D element, but it is not satiesfing condition 
    of combinationLength == 9 and for loop is out of scope because it itself last element, so it will return combinationList 
    from last statement.

    Note : for python we don't require popping after recursive method
    :param charArray: characters array from that we want combination
    :param combinationLength: what length of combination we want
    :param combinationValue: Single combination value
    :param combinationList: List of combinations
    :param offset: offset use to do not iterate loop from start as we want our combination unique.
    :return:
    """
    if combinationLength == 0:
        combinationList.append(combinationValue)
        return combinationList
    for index in range(offset, len(charArray)):
        # For understanding uncomment below Debug statements
        # print("Char array length: ", len(charArray))
        # print("Index: ", charArray[index])
        # print(" index ", index)
        # print("offset: ", offset)
        # print("combinationValue: ", combinationValue)
        # print("combinaitionLength: ", combinationLength)
        combinationValueFormatList = list(combinationValue)
        combinationValueFormatList.append(charArray[index])  # Appending value to combination
        print("combinationValue: ", combinationValueFormatList)
        # which is helping us not to remove elements from final list when we popped.
        combination(charArray, combinationLength - 1, tuple(combinationValueFormatList), combinationList, index + 1)
        # combinationPopList = list(combinationValueFormatList)
        # print("After recursion ", combinationValueFormatList)
        # Commenting pop here as we are not required
        # combinationValueFormatList.pop()  # Popping value from combination, after recursive combination operation done
        # tuple(combinationValueFormatList.pop())
    return combinationList


def permutation(charArray, permutationLength, permutationValue=(), permutationList=[], offset=0):
    """
    Method generate all combinations of elements from given array, it uses recursion inside iteration of array elements.
    
    So for every i th element we are calling recursive method which has parameter of decreasing length of combination and storing that i th element as a 
    combination appended result value.
    At last when size reduced to 0 we are returning appended combination value. Then we are doing return statement, which routes to
    last most recursive method and iteration present in that recursive method will either go to next element or return. This will be 
    there for each recursive call.

    This method does not pick duplicate elements like for a,b,c,d,e data with length 3 it will not consider a,a,a hence
    we used offset which tells loop to start with next element from previous loop.

    Also we need to return collected combination so we are using list and tuple here. as we cannot pass list in recursion
    method because pass by reference update issue, we are passing tuple here so it can have it's individual values.
    Example: a, b, c, d : combinationLength = 3
    1st iteration: a, b, c
    2nd iteration: a, b, d
    3rd iteration: a, c, d
    4th iteration: b, c, d
    
    When there is no more elements to iterate, we are returning combinationList. Example: 
    for above example, after 3rd iteration for C element loop will go to next D element, but it is not satiesfing condition 
    of combinationLength == 9 and for loop is out of scope because it itself last element, so it will return combinationList 
    from last statement.

    Note : for python we don't require popping after recursive method
    :param charArray: characters array from that we want combination
    :param combinationLength: what length of combination we want
    :param combinationValue: Single combination value
    :param combinationList: List of combinations
    :param offset: offset use to do not iterate loop from start as we want our combination unique.
    :return:
    """
    if permutationLength == 0:
        permutationList.append(permutationValue)
        return permutationList
    for index in range(offset, len(charArray)):
        # For understanding uncomment below Debug statements
        # print("Char array length: ", len(charArray))
        # print("Index: ", charArray[index])
        # print(" index ", index)
        # print("offset: ", offset)
        # print("combinationValue: ", combinationValue)
        # print("combinaitionLength: ", combinationLength)
        permutationValueFormatList = list(permutationValue)
        if charArray[index] in permutationValueFormatList:
            continue
        permutationValueFormatList.append(charArray[index])  # Appending value to combination
        # print("combinationValue: ", combinationValueFormatList)
        # which is helping us not to remove elements from final list when we popped.
        permutation(charArray, permutationLength - 1, tuple(permutationValueFormatList), permutationList, 0)
        # combinationPopList = list(combinationValueFormatList)
        # print("After recursion ", combinationValueFormatList)
        # Commenting pop here as we are not required
        # combinationValueFormatList.pop()  # Popping value from combination, after recursive combination operation done
        # tuple(combinationValueFormatList.pop())
    return permutationList



combi = combination(['a', 'b', 'c', 'd'], 2)
for i in combi:
    print(i)
print("==============================")
permu = permutation(['a', 'b', 'c', 'd'], 2)
permuCount = 0
for i in permu:
    permuCount += 1
    print(i)
permuInter = permutations(['a', 'b', 'c', 'd'], 2)
permuInterCount = 0
for i in permuInter:
    permuInterCount += 1
    print(i)
print("==============================")
print("Permu count: ", permuCount)
print("Permu inter count: ", permuInterCount)