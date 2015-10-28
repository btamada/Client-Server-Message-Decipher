#!/usr/bin/python

import socket, errno, time
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

    if not plain_text:
        return "ERROR"

    decipher_list = []

    for text in plain_text:
        if(text in trie):
            decipher_list += trie.prefixes(text)

    decipher_text = " ".join(decipher_list)

    # Pad the decipher text with spaces until its length
    # is a multiple of 16 to send back via the socket to the client
    if(len(decipher_text) % 16 != 0):
        while(len(decipher_text) % 16 != 0):
            decipher_text += " "

    return decipher_text

# Create the Trie Data Structure
trie = Trie([u'this', u'is', u'a', u'test', u'testicular', u'apple', u'istanbul',
             u'thisser', u'secret', u'message', u'massage', u'hello'])

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind((socket.gethostname(), 12345))
mysocket.listen(1)
conn, addr = mysocket.accept()
print('Connected to', addr)

while True:
    try:
        client_msg = conn.recv(4096)
        if not client_msg:
            conn.close()
            break
        else:
            plain_text = str(decrypt(client_msg).decode('ascii'))
            list_plain_text = plain_text.split(" ")
            decipher_text = decipher(list_plain_text)
            conn.sendall(encrypt(decipher_text))
            mysocket.close()
            conn.close()
            break
    except (socket.error, socket.timeout) as e:
            print(e)
            mysocket.close()
            conn.close()
            break
