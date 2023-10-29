# Convert URL to hash using any hashing algorithm
# Convert hashed value to base10
# Convert base10 values to base62\
# To convert base10 to base62, divide base10 by 62 and collect the remainders until the quotient becomes zero.
# Convert remainders to base62 equivalent value example Z = 61, 1 = 1, 0 = 0. Base 62 starts index from 0 to 61 with mapping
# as 0,1,2...Y,Z.
# While converting to tiny-url, take last remainder as first value
