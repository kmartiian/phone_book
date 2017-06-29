#server 'sinhronny'
import socket
import select

def handle(c):
	data = c.recv(1024)
	if not data:
		connections.remove()
		c.close()
		return
	print(data)
	c.sendall(data)

s = socket.socket()
s.bind(('127.0.0.1', 5000)) # local socket
s.setblocking(False)
s.listen(5)
connections =[s]
print('Waiting for connection...')
while True:  # цикл событий
	reading_sockets, _, _ = select.select(connections, [], [])
	for r_socket in reading_sockets:
		if r_socket == s:
			c, a = s.accept()
			print('Connected', a)
			connections.append(c)
		else:
			handle(r_socket)
	
