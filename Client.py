#!/usr/bin/python

__author__ = 'User1'

import socket
import Tkinter

top = Tkinter.Tk()

L1 = Tkinter.Label(top, text="User Name")
L1.pack(side = Tkinter.LEFT )
E1 = Tkinter.Entry(top, db = 5)

E1.pack(side = Tkinter.RIGHT)

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