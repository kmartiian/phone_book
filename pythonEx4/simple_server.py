#1 echoServer:

import socket

s = socket.socket()
s.bind(('127.0.0.1',)) # local socket
s.listen(5)
print('Waiting for connection...')
c, a = s.accept()
print('Connected', a)
data = c.recv()
print(data)
c.sendall(data)
c.close()
s.close()