#!/usr/bin/python

__author__ = 'Bryan Tamada'

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

# create the socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
mysocket.connect((socket.gethostname(), 12345))

# send the message to the server
mysocket.sendall(encrypt("This my secretss"))

# receive and store the response from the server in 1024 bit chunks
server_response = mysocket.recv(1024)

# close the socket
mysocket.close()

# print out the server response message
print('Received response from server %s' % decrypt(server_response).decode('ascii'))