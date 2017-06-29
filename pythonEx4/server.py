#server 'sinhronny'
import socket
import threading

def handle(c):
	while True:
		data = c.recv(1024)
		if not data:
			c.close()
			return
		print(data)
		c.sendall(data)

s = socket.socket()
s.bind(('127.0.0.1', 5000)) # local socket
s.listen(5)
print('Waiting for connection...')
while True:
	c, a = s.accept()
	print('Connected', a)
	t = threading.Thread(target=handle, args=(c,))
	t.start()
	
