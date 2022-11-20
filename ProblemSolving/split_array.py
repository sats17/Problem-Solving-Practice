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

def print_progress(arr, val):
    print(arr)
    for i in range(0, 40, 3):
        print(i)

if __name__ == '__main__':
    # arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
    arr = list(range(1, 40))
    print("generated array ", arr)
    print_progress(arr, 10)
    # resp = split(arr, 45)
    # resp = np.array_split(arr, 7)
    # for i in resp:
    #     print(i)
    #     print(type(i))
    #     print(type(i.tolist()))
