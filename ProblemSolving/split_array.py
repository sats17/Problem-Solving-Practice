import numpy as np
import math


def split(array, size):
    resp_list = []
    divider = math.ceil(len(array) / size)
    temp_divider = 0
    for i in range(size):
        if i == size - 1:
            resp_list.append(array[temp_divider:])
        else:
            resp_list.append(array[temp_divider:temp_divider + divider])
        temp_divider += divider
    return resp_list

if __name__ == '__main__':
    # arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
    arr = list(range(1, 120))
    print("generated array ", arr)
    resp = split(arr, 45)
    for i in resp:
        print(i)
