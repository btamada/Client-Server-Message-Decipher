#!/usr/bin/python

from Crypto.Cipher import AES
import socket

def encrypt(secret):
    encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    cipher_text = encryption_suite.encrypt(secret)
    return cipher_text

def decrypt(cipher):
    decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    plain_text = decryption_suite.decrypt(cipher)
    return plain_text

def decipher(plain_text):
    # insert algorithm to decipher the plain_text



    # return the resulting text
    decipher_text = "this is the result"
    return decipher_text


# create the socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bring the host name of the server and the port to listen to
mysocket.bind((socket.gethostname(), 12345))

# listen to the port and accept 1 request from the client
mysocket.listen(1)

# accept() returns the socket object and client socket address
conn, addr = mysocket.accept()

print('Connected to', addr)

# receive the secret message from the client in 1024 blocks
client_msg = conn.recv(1024)

# decrypt the client message
plain_text = decrypt(client_msg)

#decipher the client message
decipher_text = decipher(plain_text)

# send the message back to the client
conn.sendall(encrypt(decipher_text))

# close the socket
conn.close()