#!/usr/bin/python

__author__ = 'User1'

import socket

top.mainloop()

host = socket.gethostname()

# the port the server is listening on
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.sendall(b'Hello, world')

data = s.recv(1024)

s.close()

print('Received', repr(data))