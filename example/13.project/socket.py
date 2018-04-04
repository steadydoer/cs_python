import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen(1)
print ('Socket Listen Start')

connector, addr = s.accept()

while 1:
	data = connector.recv(1024)
	if not data: break

	print ("Received Message :", data.decode('utf-8'))

	data = input("Message : ")
	connector.send(data.encode('utf-8'))

s.close()
