import socket, sys

HOST = '10.30.117.175'
#HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
	data = input("Message : ")
	s.send(data.encode('utf-8'))

	data = s.recv(1024)
	if not data: break

	print ("Received Message :", data.decode('utf-8'))

s.close()
