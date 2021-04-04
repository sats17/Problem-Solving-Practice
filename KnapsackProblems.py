from itertools import combinations

# Description of algorithm - https://en.wikipedia.org/wiki/Knapsack_problem

# Problem 1 - https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the
knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents knapsack capacity,
find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
'''

'''
Input -
1) value[] - Array of values.
2) weight[] = Array of weights, respected to values.
3) W = Maximum weight that need to fit in sack
Output = 
Returns addition of values have addition of respective weights is less or equals.[Largest addition should be return]
If no any value have less weight than return then return 0.
example output link = https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
Function definition - 
 fun(value[], weight[], W)
'''

'''
Solution = 
1) Get all combination from list of values
'''



def getCombinations(values):
    for combo in combinations(values, 2):  # 2 for pairs, 3 for triplets, etc
        print(combo)


# Solution 1 = Basic linear solution

def basicLinearSol(values, weights, W):
    print("Values are ", values, "\nWeights is ", weights, "\nW is ", W)
    valuesLen = len(values)
    print(valuesLen)
    resultDict = {}
    for i in range(1, valuesLen + 1):
        print(i)
        C = i
        j = 0
        while j < valuesLen:
            j = j + 1

    return 0


values = [60, 100, 120, 122, 129]
weight = [10, 20, 30, 10, 20]
'''
5 digit combination values
60,100,120,122,129

4 digit combination for values
60,100,120,122
60,100,120,129
60,100,122,129
60,120,122,129
100,120,122,129

60,100,120,122 =1 
100,120,122,129- 5
120,122,129,60-4
122,129,60,100-3
129,60,100,120=2

60,100,120,122,129
3 digit combination for values
60,100,120
100,120,122
120,122,129
122,129,60
129,60,100

60,100,120
60,100,122
60,100,129
60,120,122
60,122,129
100,120,122
100,120,129
120,122,129

'''

# var
# letters = [1, 2, 3, 4];
#
# var
# combi = [];
# var
# temp = "";
#
# var
# letLen = Math.pow(2, letters.length);
#
# for (var i = 0; i < letLen; i++){
#     temp= "";
# for (var j=0;j < letters.length;j++) {
# / * console.log("J = ", j)
# console.log("I =", i)
# console.log("pow = ", Math.pow(2, j)) * /
# if ((i & Math.pow(2, j))){
# temp += letters[j]
# console.log("J = ", j)
# console.log("I =", i)
# console.log("pow = ", Math.pow(2, j))
# console.log("temp = ", temp)
# }
# }
# if (temp != = "") {
# combi.push(temp);
# }
#
# }
#
# if (2){
# console.log("0 is true")
# }
#
# console.log(combi.join("\n"));
# console.log(combi)
# console.log(combi.length)
# console.log(letLen)

W = 50
# response = basicLinearSol(values, weight, W);
# getCombinations(values)
if 2 and 4:
    print("hello")
a = 8 + 28 + 56 + 70 + 56 + 28 + 8 + 1
print(a)
test = [12,13,14,15]
count = 0

def combination(n, r):
    # yield 1
    # for i in range(0,3):
    #     print("inside function ",i)
    #     yield i

    print("hagh",list(range(3)))

# for i in combination(test, 2):
#     print(i)

for i in range(2,3):
    for combo in combinations(test, i):  # 2 for pairs, 3 for triplets, etc
        print(i,"th combinations /n",combo)
        count += 1
# def rSubset(arr, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    # return list(combinations(arr, r))


# for combo in range(1,12):  # 2 for pairs, 3 for triplets, etc
#     resp = rSubset(test,combo)
#     print(resp)
#     print(len(resp))
#     count += len(resp)
# print("total ",count)
# def test():
#     # return "asf"
#     yield 1
#     yield 2
# for i in test():
#     print(i)
