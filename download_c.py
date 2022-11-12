import socket
import os

s = socket.socket()
s.connect(('127.0.0.1',8001))

def sendfile(s):
    fiilname=s.recv(1024)encode('utf-8')
    print('The server requests my file:',filename)
    if os.path.exists(filename):
        print('I have %s, begin to sent!' % filename)  
        s.send(b'yes')
        s.recv(1024)
        with open(filename,'rb')as f :
            while True:
        	   data=f.read(1024)
        	   s.send(data)
        	   if len(data)<1024:
            	   break
        print('%s is sent successfully!'%filename)
    else:
        print('Sorry, I have no %s' % filename)
        s.send(b'no')

while True:
    sendfile(s)
    
s.close()