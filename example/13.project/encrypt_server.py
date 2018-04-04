import socket, sys, math

def string_xor(data, key):
	j = 0
	result = ''

	for i in range(len(data)):
		result += chr(ord(data[i]) ^ ord(key[j]))
		j += 1
		if(j == len(key)):
			j = 0

	return result

key = "password"	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen(1)
print ('Socket Listen Start')

connector, addr = s.accept()

while 1:
	data = connector.recv(1024)
	if not data: break

	decryptMessage = string_xor(data.decode('utf-8'), key)
	print ("Received Message :", decryptMessage)

	data = input("Message : ")
	encryptMessage = string_xor(data, key)
	connector.send(encryptMessage.encode('utf-8'))

s.close()
