"""
Function Description-

Complete the icecreamParlor function in the editor below. It should return an array containing the indices of the prices
of the two flavors they buy, sorted ascending.

icecreamParlor has the following parameter(s):

    m: an integer denoting the amount of money they have to spend
    cost: an integer array denoting the cost of each flavor of ice cream


Sample Input
2
4
5
1 4 5 3 2
4
4
2 2 4 3

Sample Output

1 4
1 2

"""


def icecreamParlor(m, arr):
    length = len(arr)
    result = []
    for coin in range(0,length):
        print(arr[coin])
        if(arr[coin] < m and arr[coin] != 0):
            for nextCoin in range(coin + 1,length):
                print("arr",arr[nextCoin])
                if(arr[coin]+arr[nextCoin] == m):
                    print("Got them = ", arr[coin] ," + ",arr[nextCoin])
                    print("Position = ",coin + 1," ,",nextCoin + 1)
                    result.append(coin + 1)
                    result.append(nextCoin + 1)
                    return result


if __name__ == "__main__":
    icecreamParlor(4,[1,4,5,3,2,1])