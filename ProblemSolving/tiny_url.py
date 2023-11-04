# Convert URL to hash using any hashing algorithm, also not to make hash collision use unique id generator on top of this.
# Convert hashed value to base10. Since we used hashing algorithms, hashing algorithm can have alphabets hence we are converting to base10.
# So, it is easy to convert base62.
# Convert base10 values to base62\
# To convert base10 to base62, divide base10 by 62 and collect the remainders until the quotient becomes zero.
# Convert remainders to base62 equivalent value example Z = 61, 1 = 1, 0 = 0. Base 62 starts index from 0 to 61 with mapping
# as 0,1,2...Y,Z.
# While converting to tiny-url, take last remainder as first value


"""
We are not using hash values in this TinyUrl program
"""
class TinyUrlWithBase62:
    storage = {}
    def generate_unique_id(self):
        if len(self.storage) != 0:
            return list(self.storage)[-1] + 1
        else:
            return 0
    
    def store_url_in_storage(self, id, tinyUrlId, fullUrl):
        data = {tinyUrlId: fullUrl}
        self.storage[id] = data

print("Started")
tinyUrl = TinyUrl()
id = tinyUrl.generate_unique_id()
print(id)
tinyUrl.store_url_in_storage(id, "ABAW", "https://www.github.com/sats17")
print(tinyUrl.generate_unique_id())
