__author__ = 'User1'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 9999))

s.listen(5)

conn, addr = s.accept()

print('Establishing a connection on (host/IP, port) - ', addr)

while True:
    data = conn.recv(1024)
    if not data: break

    conn.sendall(data)

# close the socket
conn.close()