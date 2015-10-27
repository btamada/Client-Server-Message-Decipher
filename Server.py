#!/usr/bin/python

import socket
import sys
from Crypto.Cipher import AES
from marisa_trie import Trie

def encrypt(secret):
    encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    cipher_text = encryption_suite.encrypt(secret)
    return cipher_text

def decrypt(cipher):
    decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    plain_text = decryption_suite.decrypt(cipher)
    return plain_text

def decipher(plain_text):

    if(plain_text == ""):
        return plain_text

    decipher_text = ""

    # insert algorithm to decipher the plain_text
    text_list = plain_text.split()

    for text in text_list:
        if(text in trie):
            decipher_text += str(trie.prefixes(text))

    # Pad the decipher text to make it a multiple of 16 in length
    if(len(decipher_text) % 16 != 0):
        while(len(decipher_text) % 16 != 0):
            decipher_text += " "

    return decipher_text

# Create the Trie Data Structure
trie = Trie([u'this', u'is', u'a', u'test', u'testicular', u'apple', u'istanbul',
             u'thisser', u'secret', u'message', u'massage'])

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((socket.gethostname(), 12345))
    mysocket.listen(1)
    conn, addr = mysocket.accept()
    print('Connected to', addr)
    client_msg = conn.recv(1024)
    if not client_msg:
        sys.exit(1)
    plain_text = decrypt(client_msg)
    decipher_text = decipher(str(plain_text))
    conn.sendall(encrypt(decipher_text))
    conn.close()
except socket.error as e:
    print(e)
    sys.exit(1)