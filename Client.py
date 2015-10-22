#!/usr/bin/python

from tkinter import *
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

def sendMsgtoSvr():
    # create the socket
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    mysocket.connect((socket.gethostname(), 12345))


    # send the message to the server
    mysocket.sendall(encrypt(encryptTxtBox.get()))

    # receive and store the response from the server in 1024 bit chunks
    server_response = mysocket.recv(1024)

    # set the result label to the server response
    result.set(decrypt(server_response).decode('ascii'))

    # close the socket
    mysocket.close()


# ======= START PROGRAM =======

# Client GUI
root = Tk()
frame = Frame(root)
frame.pack()

encryptLbl = Label(root, text="Secret Message:")
encryptLbl.pack(side=LEFT)

encryptTxtBox = Entry(root, bd=5)
encryptTxtBox.pack(side=LEFT)

result = StringVar()
resultLbl = Label(root, textvariable=result, relief=RAISED)
resultLbl.pack(side=LEFT)

encryptBtn = Button(root, text="Send to Server", command=sendMsgtoSvr)
encryptBtn.pack(side=LEFT)

root.mainloop()

# ======= END PROGRAM =======