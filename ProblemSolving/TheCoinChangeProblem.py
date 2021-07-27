def getWays(n, c):
    print(n)
    print(c)
    calculate(n,c[1])

def calculate(number,subnumber):
    count = 0
    tempNum = subnumber
    while(subnumber < number):
        subnumber += tempNum
        print(subnumber)
    if(subnumber == number):
        print("yes addtion is doing")


if __name__ == "__main__":
    getWays(4,[1,2,3])