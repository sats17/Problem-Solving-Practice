"""
Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Sample Output

YES
NO

"""
# Calculate simple interest
def simpleInterest(p, t, r):   
    return (p * t * r) / 100


# Calculate is negative number or not
def isNegative(n):
    return n < 0

def calculatePercentage(n):
    return (n * 100) / 100

def calculateHashString(n):
    return hash(n)

print(calculateHashString("Hello"))

def angryProfessor(k, a):
    totalPresent = 0

    for i in a:
        if i <= 0:
            totalPresent += 1
    print(totalPresent)
    if totalPresent >= k:
        return 'NO'
    else:
        return 'YES'
    # return("YES" if sum([1 for x in a if x <= 0]) < k else "NO")

if __name__ == "__main__":
    arr = [70,-92,42,33,-43,50,-85,20,40,47,-83,-94,30,-63,20,38,92,22,85,94,8,2,-84,87,-57,-2,
           48,86,40,-51,56,-54,72,82,-88,37,-20,-94,-14,82,-69,15,-84,-99,54,36,92,58,23,-21,-69,
           60,2,-47,89,-39,17,75,-11,78,-77,76,-61,33,27,99,-16,39,67,86,67,-66,35,-37,19,-12,34,
           17,-74,31,8,51,-42,47,-76,69,-63,-31,-80,97,88,-96,1,69,16,82,-82,-2,-23,-90]
    result = angryProfessor(52,arr)
    print(result)