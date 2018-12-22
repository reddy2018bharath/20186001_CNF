import socket

def Main():
	host = '10.1.135.147'
	port = 2148

	s = socket.socket()
	s.connect((host, port))

	message = input("->")
	while message != 'q':
		s.send((message).encode())
		data = s.recv(1024).decode()
		print("received from server:" + str(data))
		message = input()
	s.close()

if __name__ == '__main__':
	Main()