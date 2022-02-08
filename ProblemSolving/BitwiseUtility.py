def integerToBinary(n):
    # Divide n by 2 and append remainder to the end of the list
    # until n is 0.
    result = ""
    while n > 0:
        answer = n % 2
        result = str(answer) + result
        n = n // 2
    return result
# Convert integer to byte array
def integerToByteArray(n):
    # Convert integer to binary string
    binary = integerToBinary(n)
    # Convert binary string to byte array
    byteArray = []
    for i in range(0, len(binary), 8):
        byteArray.append(int(binary[i:i+8], 2))
    return byteArray

a = "123"
a_bytes = bytes(a, "ascii")
for x in a_bytes:
    print(type(x))
    print("{0:b}".format(x))
print(' '.join(["{0:b}".format(x) for x in a_bytes]))
print(integerToByteArray(123))
print(integerToBinary(1))