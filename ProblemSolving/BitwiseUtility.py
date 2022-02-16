from string import ascii_lowercase
from string import ascii_uppercase

def integerToBinary(n):
    # Divide n by 2 and append remainder to the end of the list
    # until n is 0.
    result = ""
    while n > 0:
        answer = n % 2
        result = str(answer) + result
        n = n // 2
    return result
def stringToBinary(n):
    # Convert each character of the string to its binary representation.
    # Concatenate the results.
    result = ""
    for character in n:
        asciiValue = ord(character)
        result = result + integerToBinary(asciiValue)
    return result

def getAsciiNumber(n):
    return ord(n)

def getCharPosition(n):
    # Get the position of the character in the alphabet.
    # Return the position as an integer.
    try:
        return ascii_lowercase.index(n)
    except ValueError:
        return ascii_uppercase.index(n)

def getStringAlphabetNumbers(n):
    result = []
    for i in n:
        result.append(getAsciiNumber(i))
    return result

def getBasicHash(n):
    # Get the basic hash of the string.
    # Return the hash as an integer.
    result = 0
    numbers = getStringAlphabetNumbers(n)
    for i in numbers:
        result = result + i * 5
    return result


print(getBasicHash("ac"))
print(getBasicHash("ab"))



a = "sa"
print("A binary = ", stringToBinary(a))
