from socket import *
from tkinter import *
import tkinter

IP=''
PORT = 50000
BUFLEN = 512

listenSocket = socket(AF_INET, SOCK_STREAM)

listenSocket.bind((IP, PORT))

listenSocket.listen(8)
print(f'服务端启动成功,在{PORT}端口等待客户端连接...')

dataSocket, addr = listenSocket . accept()
print('接受一个客户端连接:', addr)

while True:
    recved = dataSocket.recv(BUFLEN)
    if not recved:
        break

    info = recved.decode()
    print(f'收到对方信息: {info}' )
    dataSocket.send(f'服务端接收到了信息{info}'. encode())

dataSocket . close()
listenSocket. close()

window =tkinter.Tk()
window.title('serverOperation')
window.geometry('1000x200')

button=tkinter.Button(window,text='主机上操作',bg='#CC33CC', command=lambda : server())
button.pack()

top=mainloop()