from time import strftime, localtime

def convert(sceonds):
	return strftime('%Y-%m-%d_%H:%M:%S',localtime(sceonds))

print(convert(10))
