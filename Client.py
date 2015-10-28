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
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mysocket.connect((socket.gethostname(), 12345))
    #mysocket.setblocking(0)
    secret_message = encryptTxtBox.get()

    if not secret_message:
        result.set("ERROR: Invalid Input")
    else:
        # pad the secret message with spaces if it is not
        # 16 characters in length
        if (len(secret_message) % 16 != 0):
            while (len(secret_message) % 16 != 0):
                secret_message += " "

    try:
        mysocket.sendall(encrypt(secret_message))
        server_response = mysocket.recv(4096)
        if server_response:
            result.set(decrypt(server_response).decode('ascii'))
            mysocket.close()
        else:
            result.set("ERROR: Invalid Input")
            mysocket.close()
    except (socket.error, socket.timeout) as e:
        print(e)
        mysocket.close()
        sys.exit(1)

def quitProgram():
    root.destroy()

# Client GUI
root = Tk()
root.wm_title("Secret Messenger")

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