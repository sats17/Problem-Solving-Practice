def integerToBinary(n):
    # Divide n by 2 and append remainder to the end of the list
    # until n is 0.
    result = ""
    while n > 0:
        answer = n % 2
        result = str(answer) + result
        n = n // 2
    return result

print(integerToBinary(13))