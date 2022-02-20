def findFibbonaci(cache, n):
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
        firstFibb = findFibbonaci(cache, n-1)
        secondFibb = findFibbonaci(cache, n-2)
        answerFibb = firstFibb + secondFibb
        cache[n] = answerFibb
        return answerFibb

def Fibonacci(n):
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
        return Fibonacci(n-1) + Fibonacci(n-2)

# print(findFibbonaci({}, 15))
print(Fibonacci(15))