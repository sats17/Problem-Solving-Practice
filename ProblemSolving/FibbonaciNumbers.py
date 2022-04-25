def findFibbonaciUsingMemoization(cache, n):
    """
    Memoization is a technique to speed up the recursive calls. Using this cache we are 
    storing results for each fibbonaci number. And passing the cache as an argument to the function.
    So we can avoid the recursive calls.
    """
    if cache.get(n) is not None:
        print("Returning data from cache for ",n)
        return cache[n]
    if n == 0:
        cache[n] = 0
        print("Returning data from actual call ",n)
        return 0
    elif n == 1:
        cache[n] = 1
        print("Returning data from actual call ",n)
        return 1
    else:
        print("Returning data from actual call ",n)
        firstFibb = findFibbonaciUsingMemoization(cache, n-1)
        secondFibb = findFibbonaciUsingMemoization(cache, n-2)
        answerFibb = firstFibb + secondFibb
        cache[n] = answerFibb
        return answerFibb

def findFibonacciRecursion(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        print("Returning data from actual call constant 0 ",n)
        return 0
    elif n == 1 or n == 2:
        print("Returning data from actual call constant ",n)
        return 1
    else:
        print("Returning data from actual call ",n)
        return findFibonacciRecursion(n-1) + findFibonacciRecursion(n-2)

# print(findFibbonaciUsingMemoization({}, 15))
print(findFibonacciRecursion(4))