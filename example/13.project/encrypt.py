import math
def string_xor(data, key):
	repeat = math.ceil(len(data)/len(key))
	repeatKey = key * repeat
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(data, repeatKey))

key = "123"
data = "Hello World"

print ("Plain Text : "+data)

encryptText = string_xor(data, key)
print("Encrypt Text : "+ encryptText)

decryptText = string_xor(encryptText, key)
print ("Decrypt Text : "+ decryptText)
