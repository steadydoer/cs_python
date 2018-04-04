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

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
	data = input("Message : ")
	encryptMessage = string_xor(data, key)
	s.send(encryptMessage.encode('utf-8'))

	data = s.recv(1024)
	if not data: break

	decryptMessage = string_xor(data.decode('utf-8'), key)
	print ("Received Message :", decryptMessage)

s.close()
