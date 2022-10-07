from socket import *
from tkinter import *
import tkinter

IP = '127.0.0.1'
SERVER_PORT = 50000
BUFLEN = 1024

dataSocket = socket(AF_INET, SOCK_STREAM)

dataSocket.connect((IP, SERVER_PORT))

while Ture:
	toSend = input('>>>')
	if toSend =='exit':
		break

	dataSocket.send(toSend.encode())

	recved = dataSocket.recv(BUFLEN)
	if not recved:
		break
	print(recved.decode())

dataSocket.close()

window =tkinter.Tk()
window.title('clientOperation')
window.geometry('1000x200')

button=tkinter.Button(window,text='在客户机操作',bg='#CC33CC', command=lambda : client())
button.pack()
top=mainloop()
