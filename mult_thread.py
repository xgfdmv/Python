import threading

def print_numbers(start,end):
	for num in range(start,end):
		print (num)

t1 = threading.Thread (target=print_numbers,args=(1,8))
t2 = threading.Thread (target=print_numbers,args=(11,18))

t1.start()
t2.start()

for num in range(21,28):
	print (num)

