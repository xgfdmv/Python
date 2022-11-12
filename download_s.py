import socket

s = socket.socket()
s.bind(('127.0.0.1',8001))
s.listen(2)
print('Waiting for connect...')

conn,addr = s.accept()
print('Connected:'+str(addr))

while True:
	filename='C:/Users/bjyx/test.txt'
	print('I want to get the file %s!' % filename)
	conn.send(filename.encode('utf-8'))
	str1 = conn.recv(1024)
	str2 = str1.decode('utf-8')
	if str2 == 'no':
		print('No %s ' % filename)
	else:
		conn.send(b'I am ready!')
		temp = filename.split('/')#把/去掉
		myname = 'my_' + temp[len(temp)-1]
		with open(myname,'wb')as f:
			while True:
				data = conn.recv(1024)
				f.write(data)
				if len(data)<1024:
					break
	print('The download file is %s',myname)

conn.close()
s.close()
