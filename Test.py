from tkinter import *

# Client GUI
root = Tk()

encryptLbl = Label(root, text="Secret Message:")
encryptTxtBox = Entry(root, bd=5)

result = StringVar()
resultLbl = Label(root, textvariable=result, relief=RAISED)

encryptBtn = Button(root, text="Send to Server")

encryptLbl.grid(row=0, column=0)
encryptTxtBox.grid(row=0, column=1)
encryptBtn.grid(columnspan=2)
resultLbl.grid(columnspan=2)

root.mainloop()