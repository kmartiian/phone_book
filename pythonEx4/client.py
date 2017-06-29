#client
import time
import socket

s = socket.socket()
s.connect(('127.0.0.1', 5000))
while True:
	s.sandall(b'Hello')
	data = s.recv(1024)
	print('Client:', data)
	time.sleep(2)
	
