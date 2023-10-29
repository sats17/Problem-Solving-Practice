# Convert URL to hash using any hashing algorithm, also not to make hash collision use unique id generator on top of this.
# Convert hashed value to base10
# Convert base10 values to base62\
# To convert base10 to base62, divide base10 by 62 and collect the remainders until the quotient becomes zero.
# Convert remainders to base62 equivalent value example Z = 61, 1 = 1, 0 = 0. Base 62 starts index from 0 to 61 with mapping
# as 0,1,2...Y,Z.
# While converting to tiny-url, take last remainder as first value


import hashlib

def hash_string(input_string):
    # Encode the string to bytes (UTF-8 encoding is commonly used)
    encoded_string = input_string.encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the encoded bytes
    sha256_hash.update(encoded_string)
    
    # Get the hexadecimal representation of the hash
    hashed_string = sha256_hash.hexdigest()
    
    return hashed_string

# Example usage
input_string = "Hello, World!"
hashed_string = hash_string(input_string)

print(f"The hash of '{input_string}' is: {hashed_string}")
