def split(array, size):
    divider = len(array) // size
    print(len(array))
    print(divider)
    temp_divider = 0
    for i in range(size):
        print("temp_divider ",temp_divider)
        if i == size - 1:
            print(array[temp_divider:])
        else:
            print(array[temp_divider:temp_divider + divider])
        temp_divider += divider
    # for i in range(0, len(array) - 1, divider):
    #     print(array[i])
    #     print(i)
    #     print(divider)
    #     print(array[i: i + divider])


if __name__ == '__main__':
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    split(arr, 8)
