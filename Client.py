#!/usr/bin/python

from tkinter import *
from Crypto.Cipher import AES
import socket
import sys

def encrypt(secret):
    encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    cipher_text = encryption_suite.encrypt(secret)
    return cipher_text

def decrypt(cipher):
    decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    plain_text = decryption_suite.decrypt(cipher)
    return plain_text

def sendMsgtoSvr():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((socket.gethostname(), 12345))
    mysocket.sendall(encrypt(encryptTxtBox.get()))
    server_response = mysocket.recv(1024) # receive and store the response from the server in 1024 bit chunks
    result.set(decrypt(server_response).decode('ascii'))
    mysocket.close()

def quitProgram():
    root.destroy()

# Client GUI
root = Tk()

encryptLbl = Label(root, text="Secret Message:")
encryptTxtBox = Entry(root, bd=5)

result = StringVar()
resultLbl = Label(root, textvariable=result, relief=RAISED)

encryptBtn = Button(root, text="Send to Server", command=sendMsgtoSvr)

quitBtn = Button(root, text="Quit", command=quitProgram)

encryptLbl.grid(row=0, column=0)
encryptTxtBox.grid(row=0, column=1)
encryptBtn.grid(row=1, column=0)
quitBtn.grid(row=1, column=1)
resultLbl.grid(columnspan=2)

root.mainloop()